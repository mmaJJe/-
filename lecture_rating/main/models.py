from django.db import models
import random
import string

# Create your models here.

class University(models.Model) :
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Professor(models.Model) :
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Lecture (models.Model) :
    lecture_id = models.CharField(primary_key=True, max_length=20, default=''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(8)))
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class LectureRatingBoard(models.Model) :
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    def __str__(self):
        return self.title