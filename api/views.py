from django.db.models.query import QuerySet
from rest_framework import viewsets, mixins

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "name"

# class MyExport(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """ A really cool function"""

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
