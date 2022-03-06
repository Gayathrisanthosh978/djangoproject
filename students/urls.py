from django.urls import path
from students import views
urlpatterns=[
    path('student/add', views.AddStudent.as_view(), name='studadd'),
    path('student/addmark',views.AddMark.as_view(),name="addmark")

]