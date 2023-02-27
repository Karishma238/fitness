from django.db import models

# Create your models here.


class Register(models.Model):
    Name = models.CharField(max_length = 100)
    Email = models.EmailField(max_length=100)
    Phone = models.IntegerField()
    Location = models.CharField(max_length = 500)
    Message = models.TextField()

    class Meta:
        db_table = "Register"


class SignupInfo(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length = 50)
    Mobile = models.IntegerField()

    class Meta:
        db_table = "Signup"


class WorkoutCategory(models.Model):
    Cat_Image = models.ImageField()
    Cat_Logo = models.ImageField()
    Cat_Name = models.CharField(max_length=100)
    Cat_Description = models.TextField()

    def __str__(self):
        return self.Cat_Name
    
    class Mets:
        db_table = "WorkoutCategory"


class WorkoutSubcategory(models.Model):
    Image = models.ImageField()
    Lifting_Name = models.CharField(max_length=50)
    Description = models.TextField()
    Category = models.ForeignKey(to = 'WorkoutCategory', on_delete = models.CASCADE)

    class Meta:
        db_table = "WorkoutSubcategory"

    

