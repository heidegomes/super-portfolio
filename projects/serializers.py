from rest_framework import serializers
from projects.models import Profile, Project, CertifyingInstitution


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "github", "linkedin", "bio"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertifyingInstitution
        fields = "__all__"
        many = True

    def create(self, validated_data):
        certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        return certifying_institution
