from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Teacher(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    info = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Ashiqsabaq(models.Model):
    title = models.CharField(max_length=300)
    klas = models.CharField(max_length=300)
    info = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Calculate(models.Model):
    count = models.IntegerField(max_length=5)
    info = models.CharField(max_length=100)

    def __str__(self):
        return self.info



class Post(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    views = models.IntegerField()
    logo = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=1000)
    description = models.TextField()
    author = models.CharField(max_length=300,default='Admin')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=300, default='Foto - ')
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Contact(models.Model):
    adres = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    site = models.CharField(max_length=300)
    src_map = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.adres

class Gos(models.Model):
    title = models.CharField(max_length=300)

    pdf = models.FileField(blank=True,upload_to='file')

    pub_date = models.DateField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

