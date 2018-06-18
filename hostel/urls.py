from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register('/student', views.StudentView)
router.register('/hostel', views.HostelView)
router.register('/room', views.RoomView)
router.register('/dormitory', views.DormitoryView)



urlpatterns = [
    #path('', views.index, name='index'),
    path('api', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html'))

]
