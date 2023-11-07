from rest_framework import viewsets
from projects.models import Profile
from projects.serializers import ProfileSerializer


class ProfilesListViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# class CreateProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.create()
#     serializer_class = ProfileSerializer


# class IdProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.get(id=id)
#     serializer_class = ProfileSerializer


# class UpdatedProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.update(id=id)
#     serializer_class = ProfileSerializer


# class DeleteProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.delete(id=id)
#     serializer_class = ProfileSerializer
