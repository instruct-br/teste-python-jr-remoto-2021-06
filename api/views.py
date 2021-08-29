from django.db.models.query import QuerySet
from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a Project instance.

    list:
        Return all Project.

    create:
        Create a new Project.

    delete:
        Remove an existing Project.

    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "Name"


# from django.shortcuts import get_object_or_404
# from rest_framework import viewsets
# from rest_framework.response import Response

# from .models import Project
# from .serializers import ProjectSerializer


# class UserViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet that for listing or retrieving users.
#     """

#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     lookup_field = "Name"

#     def list(self, request):
#         return Response(self.serializer_class.data)
