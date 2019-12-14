from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'downtimeApp'
urlpatterns = [

    path('', views.home, name='employee_home'),
    #path('', views.employee_home, name='employee_home'),
    path('downtime_list/', views.downtime_list, name='downtime_list'),
    path('machine/create/', views.machine_new, name='machine_new'),
    path('machine/<pk>/edit/', views.machine_edit, name='machine_edit'),
    path('machine/<pk>/delete/', views.machine_delete, name='machine_delete'),
    path('downtime/create/', views.downtime_new, name='downtime_new'),
    path('downtime/<pk>/edit/', views.downtime_edit, name='downtime_edit'),

]
