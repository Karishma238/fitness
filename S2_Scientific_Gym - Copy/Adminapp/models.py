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


class SubExercise(models.Model):
    Image = models.ImageField()
    Exer_Name = models.CharField(max_length=50)
    Description = models.TextField()
    Subcategory = models.ForeignKey(to = 'WorkoutSubcategory', on_delete = models.CASCADE)

    class Meta:
        db_table = "SubExercise"


class CatExercise(models.Model):
    Image = models.ImageField()
    Exer_Name = models.CharField(max_length=50)
    Description = models.TextField()
    Category = models.ForeignKey(to = 'WorkoutCategory', on_delete = models.CASCADE)

    class Meta:
        db_table = "CatExercise"


class Exec_Sub_Info(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Subcategory = models.ForeignKey(to = 'WorkoutSubcategory', on_delete = models.CASCADE)

    class Meta:
        db_table = "Exec_Sub_Info"


class WorkoutSubcategory(models.Model):
    Image = models.ImageField()
    Sub_Name = models.CharField(max_length=50)
    Description = models.TextField()
    Category = models.ForeignKey(default=5, to = 'WorkoutCategory', on_delete = models.CASCADE)

    def __str__(self):
        return self.Sub_Name

    class Meta:
        db_table = "WorkoutSubcategory"


class Packages(models.Model):
    Duration = models.CharField(max_length=25)
    Price = models.IntegerField(default=0)
    Include = models.TextField()

    class Meta:
        db_table = "Packages"


class Trainer(models.Model):
    Name = models.CharField(max_length=50)
    Image = models.ImageField()
    Work = models.CharField(max_length=50)
    Weight = models.CharField(max_length=10)
    Height = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.IntegerField()
    Address = models.TextField()
    Specialities = models.TextField()
    Qualification = models.TextField()
    Achievement = models.TextField()
    Description = models.TextField()

    class Meta:
        db_table = "Trainer"


    

