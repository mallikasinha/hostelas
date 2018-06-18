from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Student, Hostel, Room, Dormitory
from .serializers import StudentSerializer, HostelSerializer, RoomSerializer, DormitorySerializer

class StudentView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class HostelView(viewsets.ModelViewSet):
    queryset=Hostel.objects.all()
    serializer_class = HostelSerializer

class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class DormitoryView(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer

def index(request):
    return render(request, 'index.html')
