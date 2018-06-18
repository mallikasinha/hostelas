new Vue({
  el: '#app',
  delimiters: ['${','}'],
  data: {
    registration_no: '',
    first_name: '',
    last_name: '',
    gender: '',
    address: '',
    mobile_no: null,
    program_of_study: '',
    school: '',
    rank: '',
    category: '',
    year_of_admission: '',
    duration_of_program: '',
    equivalent_degree: false,
    previous_degree_of_jnu: false,
    hostels: [],
    priorityOne: false,
    priorityTwo: false,
    priorityText: '',
    hostelId: null,
    priority: null,
    dormitorys: [],
    dormitoryId:null,
    no_of_beds: null,
    seen: true
  },
  mounted() {

  },
  methods: {
    getHostels: function() {
      axios.get('api/hostel')
      .then((response) => {
        this.hostels = response.data;
        console.log(this.hostels);
     })
     .catch((err) => {
      console.log(err);
     })
  },
  createStudent: function() {
    axios.post('/api/student/', {
      registration_no: this.registration_no,
      first_name: this.first_name,
      last_name: this.last_name,
      gender: this.gender,
      address: this.address,
      mobile_no: this.mobile_no,
      program_of_study: this.program_of_study,
      school: this.school,
      rank: this.rank,
      category: this.category,
      year_of_admission: this.year_of_admission,
      duration_of_program: this.duration_of_program,
      equivalent_degree: this.equivalent_degree,
      previous_degree_of_jnu: this.previous_degree_of_jnu,
      priority: this.priority,
      hostel: this.hostelId,
      dormitory: this.dormitoryId
    })
    .then((response) => {
      this.getHostels();
      console.log(response);
    })
    .catch((error) => {
      console.log(error);
    });
  },
  getDormitory: function() {
    axios.get('api/dormitory')
    .then((response) => {
      this.dormitorys = response.data;
      console.log(this.dormitorys);
    })
    .catch((err) => {
      console.log(err);
    })
  },
    checkPriority: function() {
      if ((this.address.match(/delhi/gi) == null) &&
          ((this.category == "ST") ||
          (this.category == "SC") ||
          (this.category == "FN") ||
          (this.category == "OBC") ||
          (this.category == "GN") ||
          (this.category == "PH")) &&
          (this.duration_of_program == "Full Time Program") &&
          (this.equivalent_degree == false) &&
          (this.previous_degree_of_jnu == false)) {
            console.log("you belong to priority 1 list");
            this.priorityOne = true;
            this.priorityTwo = false;
            this.priorityText = 'One';
            if (this.priorityText == 'One') {
              this.priority = 1;
            }
            this.getHostels();
          }
      else if((this.duration_of_program == "Partial Time Program") ||
              (this.equivalent_degree == true) ||
              (this.previous_degree_of_jnu == true))
              {
                console.log("you belong to priority 2 list");
                this.priorityOne = false;
                this.priorityTwo = true;
                this.priorityText = 'Two';
                if (this.priorityText == 'Two') {
                  this.priority = 2;
                }
                this.getDormitory();
              }

          else{
            this.priorityOne = false;
            this.priorityTwo = false;
            this.priorityText == 'you are not eligible for the hostel';
            console.log("you are not eligible for the hostel");
          }

            }
          }

  });
