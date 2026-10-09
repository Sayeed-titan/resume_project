from django.urls import path
from . import views

urlpatterns = [
    #when visits the empty path '', run the resume_list view
    path('', views.resume_list, name='resume_list')
]