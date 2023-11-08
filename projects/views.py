from rest_framework import viewsets
from projects.models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate,
)
from projects.serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertifyingInstitutionSerializer,
    CertificateSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile_id = Profile.objects.filter(id=kwargs["pk"])
            context = {"profile": profile_id}
            return render(request, "profile_detail.html", context)
        return super().retrieve(request, *args, **kwargs)


class ProjectsListViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer


class Certificate(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
