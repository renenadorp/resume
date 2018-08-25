from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timezone import now

# Create your models here.


class Person(models.Model):
    id          = models.IntegerField(primary_key=True, unique = True)   
    first_name  = models.CharField(max_length=50)
    last_name   = models.TextField(null=True, blank=True)
    active      = models.CharField(default='Y', max_length=1)
    gender      = models.CharField(default='Y', max_length=1)
    date_birth  = models.DateField(default=now(), blank=True)
    card_image  = models.CharField(max_length=100, null=True, blank=True, default='person-card-default.jpg')
    def __str__(self):
        return str(self.name)


class CV(models.Model):
    id          = models.IntegerField(primary_key=True, unique = True)
    name        = models.CharField(max_length=50)
    active      = models.CharField(max_length=1)
    card_image  = models.CharField(max_length=100, null=True, blank=True, default='cv-card-default.jpg')
    person      = models.ForeignKey(Person, on_delete=models.CASCADE    , default=-1)
    def __str__(self):
        return str(self.name)


    
class Project(models.Model):
    id           = models.IntegerField(primary_key=True, unique = True)   
    name         = models.CharField(max_length=50)
    descr        = models.TextField(null=True, blank=True)
    person       = models.ForeignKey(Person, on_delete=models.CASCADE, default=-1)
    cv           = models.ManyToManyField(CV)
    active       = models.CharField(default='Y', max_length=1)
    date_start   = models.DateField(default=now(), blank=True)
    date_end     = models.DateField(default=now(), blank=True)
    card_image   = models.CharField(max_length=100, null=True, blank=True, default='project-card-default.jpg')

    def __str__(self):
        return self.name


class SkillGroup(models.Model):
    id          = models.IntegerField(primary_key=True, unique = True)   
    name        = models.CharField(max_length=50)
    descr       = models.TextField(null=True, blank=True)
    active      = models.CharField(default='Y', max_length=1)
    card_image  = models.CharField(max_length=100, null=True, blank=True, default='skillgroup-card-default.jpg')

    def __str__(self):
        return self.name 


class Skill(models.Model):
    id          = models.IntegerField(primary_key=True, unique = True)   
    name        = models.CharField(max_length=50)
    descr       = models.TextField(null=True, blank=True)
    active      = models.CharField(default='Y', max_length=1)
    card_image  = models.CharField(max_length=100, null=True, blank=True, default='skill-card-default.jpg')
    skillgroup  = models.ForeignKey(SkillGroup, on_delete=models.CASCADE, default=-1)
    person      = models.ForeignKey(Person, on_delete=models.CASCADE, default=-1)
    cv          = models.ManyToManyField(CV)
    skill_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.name 


class Education(models.Model):
    id           = models.IntegerField(primary_key=True, unique = True)   
    name         = models.CharField(max_length=50)
    descr        = models.TextField(null=True, blank=True)
    person       = models.ForeignKey(Person, on_delete=models.CASCADE, default=-1)
    cv           = models.ManyToManyField(CV)
    active       = models.CharField(default='Y', max_length=1)
    date_start   = models.DateField(default=now(), blank=True)
    date_end     = models.DateField(default=now(), blank=True)
    card_image   = models.CharField(max_length=100, null=True, blank=True, default='education-card-default.jpg')
    completed    = models.BooleanField(default=True)
    def __str__(self):
        return self.name


