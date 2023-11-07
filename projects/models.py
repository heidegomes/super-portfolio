from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50, blank=False)
    github = models.URLField(max_length=100, blank=False)
    linkedin = models.URLField(max_length=100, blank=False)
    bio = models.TextField(blank=False)

    def __str__(self):
        return self.name
