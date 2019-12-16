from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'downtimeApp'
urlpatterns = [

    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('', views.home, name='supervisor_home'),
    path('', views.home, name='employee_home'),
    path('machine/create/', views.machine_new, name='machine_new'),
    path('machine_list/', views.machine_list, name='machine_list'),
    path('machine/<pk>/edit/', views.machine_edit, name='machine_edit'),
    path('machine/<pk>/delete/', views.machine_delete, name='machine_delete'),
    path('machine/<pk>/summary/', views.summary, name='summary'),
    path('downtime_list/', views.downtime_list, name='downtime_list'),
    path('downtime/create/', views.downtime_new, name='downtime_new'),
    path('downtime/<pk>/edit/', views.downtime_edit, name='downtime_edit'),
    url('downtimes_json/', views.DwontimeList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)