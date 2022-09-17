from email.mime import image
from django.db import models

# Create your models here.

class Information(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to = "information")
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    location = models.URLField(max_length=300)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"
    
    
class IconInformation(models.Model):
    information = models.ForeignKey(Information,on_delete=models.CASCADE)
    COLOR = (('fac','fac'),('twi','twi'),('dri','dri'),('ins','ins'),('tel','tel'))
    link_name = models.URLField(max_length=200)
    icon = models.CharField(max_length=150)
    font_color = models.CharField(choices=COLOR,max_length=150)
    def __str__(self) -> str:
        return self.icon

class SpecialistInformation(models.Model):
    specialist = models.CharField(max_length=300)
    information = models.ForeignKey(Information,on_delete=models.CASCADE)
    percentage = models.IntegerField()

    def __str__(self) -> str:
        return self.specialist

class Work(models.Model):
    icon = models.CharField(max_length=170)
    title = models.CharField(max_length=100)
    specialist = models.CharField(max_length=200)
    descriptions = models.TextField()
    information = models.ForeignKey(Information,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
class Thoughts(models.Model):
    image = models.ImageField(upload_to='thoughts')
    description = models.TextField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

class Fair_price(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(default=0)
    def __str__(self) -> str:
        return self.title

class Love_to(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.title

class Language(models.Model):
    LEVEL = (
        ('ldInner profLevel1','ldInner profLevel1'),
        ('ldInner profLevel2','ldInner profLevel2'),
        ('ldInner profLevel3','ldInner profLevel3'),
        ('ldInner profLevel4','ldInner profLevel4'),
        ('ldInner profLevel5','ldInner profLevel5'),
        ('ldInner profLevel6','ldInner profLevel6'),
        ('ldInner profLevel7','ldInner profLevel7'),
        ('ldInner profLevel8','ldInner profLevel8'),
        ('ldInner profLevel9','ldInner profLevel9'),
        ('ldInner profLevel10','ldInner profLevel10'),
        

    )
    title = models.CharField(max_length=150)
    count = models.IntegerField(default=0)
    icon = models.CharField(choices=LEVEL,max_length=150)

    def __str__(self) -> str:
        return self.title

class Brend(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='brend')

class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self) -> str:
        return self.full_name









