from django.db import models

# Create your models here.
class Client(models.Model):
    ClientId = models.AutoField(primary_key=True)
    ClientName = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)


class Project(models.Model):
    ProjectName = models.CharField(max_length=150)


class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)



