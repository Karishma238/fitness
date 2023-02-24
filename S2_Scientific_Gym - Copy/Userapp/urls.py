from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('blog', views.blog),
    path('login', views.login),
    path('membership', views.membership),
    path('workout',views.workout),
    
]
