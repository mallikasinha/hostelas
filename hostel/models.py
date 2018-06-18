from django.db import models


class Hostel(models.Model):
    hostel_name = models.CharField(max_length = 70)
    available_rooms = models.IntegerField()
    gender = models.CharField(max_length = 10)
    db_table = 'hostel'

    def __str__(self):
        return str(self.id) + ', ' + self.hostel_name + ', ' + str(self.available_rooms) + ', ' + self.gender

class Dormitory(models.Model):
    hostel = models.OneToOneField(
        Hostel,
        on_delete=models.CASCADE
    )

    dorm_name = models.CharField(max_length = 70)
    available_beds = models.IntegerField()
    gender = models.CharField(max_length = 20)
    db_table = 'dormitory'

    def __str__(self):
        return str(self.id) + ', ' +   self.dorm_name + ', ' + str(self.available_beds) + ', ' + self.gender

class Room(models.Model):
    hostel = models.ForeignKey(
        Hostel,
        on_delete=models.CASCADE
    )
    room_no = models.IntegerField()
    capacity = models.IntegerField()
    status = models.BooleanField()
    db_table = 'room'

    def __str__(self):
        return str(self.id) + ', ' + str(self.room_no) + ', ' + str(self.capacity) + ', ' + str(self.status)

class Student(models.Model):
    hostel = models.ForeignKey(
        Hostel,
        null = True,
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        Room,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    dormitory = models.ForeignKey(
        Dormitory,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    registration_no = models.CharField(max_length = 20)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    gender = models.CharField(max_length = 20)
    address = models.CharField(max_length = 70)
    mobile_no = models.IntegerField()
    program_of_study = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    rank = models.IntegerField()
    category = models.CharField(max_length = 20)
    year_of_admission = models.DateField()
    duration_of_program = models.CharField(max_length = 20)
    equivalent_degree = models.BooleanField()
    previous_degree_of_jnu = models.BooleanField()
    priority = models.IntegerField()

    db_table = 'student'

    def __str__(self):
        return str(self.id) + ', ' + self.first_name + ', ' + self.last_name + ', ' + self.address + ', ' + str(self.mobile_no) + ', ' + self.program_of_study + ', ' + self.school + ', ' + str(self.rank) + ', ' + self.category + ', ' + str(self.year_of_admission)  + ', ' + self.duration_of_program + ', ' + str(self.equivalent_degree) + ', ' + str(self.previous_degree_of_jnu) + ', ' + str(self.priority) + ', ' + str(self.hostel)
