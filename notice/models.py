from django.db import models



class Person(models.Model):
    name = models.CharField(max_length = 100)
    age = models.CharField(max_length = 50, blank = True)
    dateOfBirth = models.DateTimeField()

    def __str__(self):
        return self.name
    

class Category(models.Model):
    title = models.CharField(max_length = 100)
    class_teacher = models.CharField(max_length = 100)

    def __str__(self):
        return self.title
    

class Notice(models.Model):
    person = models.ForeignKey("Person",  on_delete=models.CASCADE)
    description = models.TextField(max_length = 500)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.description
    

class School(models.Model):
    school_name =models.CharField(max_length=50)

    def __str__(self):
        return self.school_name
    





# Create your models here.

# python manage.py migrate
# python manage.py makemigrations