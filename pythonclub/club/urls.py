from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index' ),
    path('techtypes/', views.techtypes, name='techtypes'),
    path('getmeeting/', views.getmeeting, name='getmeeting'),
    path('meetingdetail/<int:id>', views.meetingdetail, name="details"),
]
