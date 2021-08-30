import requests

from rest_framework import serializers
from rest_framework.exceptions import ParseError
from .models import PackageRelease, Project

PYPI_ROUTE = "https://pypi.org/pypi/"
content = {"error": "One or more packages doesn't exist"}


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ["name", "version"]
        extra_kwargs = {"version": {"required": False}}


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "packages"]

    packages = PackageSerializer(many=True)

    def check(self, validated_data):
        # checo se os pacotes tem nomes e versoes validos
        result = []
        packages = validated_data["packages"]
        if len(packages) == 0:
            raise ParseError(content)
        for pack in packages:
            name = pack["name"]
            try:
                version = pack["version"]
            except KeyError:
                pypi_response = requests.get(f"{PYPI_ROUTE}{name}/json/")
                if pypi_response.status_code != 200:
                    raise ParseError(content)
                json_pypi = pypi_response.json()
                version = json_pypi["info"]["version"]
            else:
                pypi_response = requests.get(
                    f"{PYPI_ROUTE}{name}/{version}/json/"
                )
            if pypi_response.status_code != 200:
                raise ParseError(content)
            else:
                result.append({"version": version, "name": name})
        validated_data["packages"] = result
        return result

    def create(self, validated_data):
        result = []
        result = self.check(validated_data)
        # salvo no banco
        try:
            project = Project(name=validated_data["name"])
            project.save()
        except TypeError:
            raise ParseError(content)
        else:
            for pack in result:
                version = pack["version"]
                name = pack["name"]
                try:
                    package = PackageRelease(
                        name=name, version=version, project=project
                    )
                    package.save()
                except TypeError:
                    raise ParseError(content)
        return project
