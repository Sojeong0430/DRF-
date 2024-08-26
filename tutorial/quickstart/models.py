from django.db import models

class Todo (models.Model):
    #pk
    name = models.CharField(max_length=10)
    content = models.TextField()
