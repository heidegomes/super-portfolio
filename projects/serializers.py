from rest_framework import serializers
from projects.models import Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "github", "linkedin", "bio"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = [
        #     "name",
        #     "description",
        #     "github_url",
        #     "keyword",
        #     "key_skill",
        #     "profile",
        # ]
        fields = "__all__"
