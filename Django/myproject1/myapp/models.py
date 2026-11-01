from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    courses =models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class Profile(models.Model):
    bio = models.TextField()
    birthdate = models.DateField(null=True, blank=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    issued_date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.PROTECT)