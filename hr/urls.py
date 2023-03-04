
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job_category', views.job_category,name='job_categoryy'),
    # email urls
    path('front_mail', views.front_mail, name='front_mail'),
    path('back_mail', views.back_mail, name='back_mail'),
    path('full_mail', views.full_mail, name='full_mail'),
    path('intern_mail', views.intern_mail, name='intern_mail'),

    #===================backend urls====================#
    path('backend/', views.backend, name="backend")
]
