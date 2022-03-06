from django.urls import path
from employees import views
urlpatterns=[
    path('emp/all', views.Listemp.as_view(), name='emplist'),
    path('emp/add', views.AddEmp.as_view(), name='empadd'),
    path('emp/<int:id>', views.ViewEmp.as_view(), name='empview'),
    path('emp/change/<int:id>', views.EditEmp.as_view(), name='empedit'),
    path('emp/remove/<int:id>', views.DelEmp.as_view(), name='empdel'),
    path('registration',views.Registration.as_view(),name='signup'),
    path('login',views.Login.as_view(),name='signin'),
]