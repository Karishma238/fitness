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
