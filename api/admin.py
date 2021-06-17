from django.contrib import admin

from .models import Project, PackageRelease

admin.site.register(Project)
admin.site.register(PackageRelease)
