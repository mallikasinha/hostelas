from rest_framework import serializers
from .models import Student, Hostel, Room, Dormitory

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('registration_no', 'first_name', 'last_name', 'gender', 'address', 'mobile_no', 'program_of_study', 'school', 'rank', 'category', 'year_of_admission', 'duration_of_program', 'equivalent_degree', 'previous_degree_of_jnu', 'priority', 'hostel', 'dormitory', 'room')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'hostel', 'room_no', 'capacity', 'status')

class HostelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hostel
        fields = ('url', 'id', 'hostel_name', 'available_rooms', 'gender',)

class DormitorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dormitory
        fields = ('url', 'id', 'hostel', 'dorm_name', 'available_beds', 'gender')
