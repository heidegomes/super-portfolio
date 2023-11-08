from rest_framework import serializers
from projects.models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate,
)


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
        fields = ["url", "certificates", "name", "id"]
        many = True

    def create(self, validated_data):
        certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        return certifying_institution


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"
        many = True

    def create(self, validated_data):
        certificate = Certificate.objects.create(**validated_data)
        return certificate
