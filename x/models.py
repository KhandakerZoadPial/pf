from django.db import models

# Create your models here.
class projects(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.TextField(blank=True)


class c(models.Model):
    name = models.CharField(max_length=100)
    frm = models.CharField(max_length=100)
