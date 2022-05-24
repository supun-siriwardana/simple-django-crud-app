from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100, null=True)
    emp_code = models.CharField(max_length=3, null=True)
    mobile = models.CharField(max_length=15, null=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)