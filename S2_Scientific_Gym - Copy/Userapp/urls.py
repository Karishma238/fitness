from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('register', views.register),
    path('blog', views.blog),
    path('login', views.login),
    path('logout', views.Signout),
    path('Signup', views.Signup),
    path('membership', views.membership),
    path('workout',views.workout),
    path('WorkoutSubcategory', views.Subcategory),
    path('SubcategoryExercise/<sid>', views.ExerciseSub),
    path('CategoryExercise/<cid>', views.ExerciseCat),
    path('trainer', views.trainer),
    path('TrainerProfile/<tid>', views.TrainerProfile),
    path('HealthyLives', views.HealthyLives),
    path('Pay', views.Pay),
]
