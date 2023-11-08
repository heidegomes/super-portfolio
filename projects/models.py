from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50, blank=False)
    github = models.URLField(max_length=100, blank=False)
    linkedin = models.URLField(max_length=100, blank=False)
    bio = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    github_url = models.URLField(max_length=50)
    keyword = models.CharField(max_length=50)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projects"
    )

    def __str__(self):
        return self.name
