from django.db import models
from django.db import models
from datetime import datetime
class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
# Create your models here.
