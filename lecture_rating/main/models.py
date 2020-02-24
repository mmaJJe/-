from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import random
import string

# Create your models here.

class University(models.Model) :
    name = models.CharField(max_length=20)
    def __str__ (self) :
        return self.name

class Professor(models.Model) :
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    def __str__ (self) :
        return self.name

class Lecture (models.Model) :
    lecture_id = models.CharField(primary_key=True, max_length=20, default=''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(8)))
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    reco = models.IntegerField(default=0)
    not_reco = models.IntegerField(default=0)
    def __str__ (self) :
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    university = models.CharField(max_length=20)
    major= models.CharField(max_length=25)
    admission_year=models.CharField(max_length=4, default=0)


class LectureRatingBoard(models.Model) :
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    semester_year = models.DateField(blank=True, null=True)
    semester = models.CharField(max_length=5, blank=True, null=True)
    pro_lecturePower = models.IntegerField(default=0)
    test_level = models.IntegerField(default=0)
    project = models.IntegerField(default=0)
    homework = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)

    def __str__(self):
        return self.lecture.name
