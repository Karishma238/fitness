from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('blog', views.blog),
    path('login', views.login),
    path('Signup', views.Signup),
    path('membership', views.membership),
    path('workout',views.workout),
    path('WorkoutSubcategory/<did>', views.Subcategory),
    path('trainer', views.trainer),
    path('TrainerProfile', views.TrainerProfile),
]
