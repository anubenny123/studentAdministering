from django.urls import path
from .views import StudentList,AddStudent


urlpatterns =[
    path('',StudentList.as_view(),name='stu-list'),
    path('addstudent/',AddStudent.as_view(),name='stu-add')
]