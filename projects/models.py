from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50, blank=False, min_length=500)
    github = models.URLField(max_length=100, blank=False, min_length=500)
    linkedin = models.URLField(max_length=100, blank=False, min_length=500)
    bio = models.TextField(blank=False, min_length=500)

    def string(self):
        return self.name
