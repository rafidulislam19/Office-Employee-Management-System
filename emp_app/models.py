from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, null=False, default=None)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False, default=None)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False, default=None)
    last_name = models.CharField(max_length=100, default=None)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)

