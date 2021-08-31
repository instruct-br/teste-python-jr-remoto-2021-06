from rest_framework import serializers

from .models import PackageRelease, Project


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'packages']

    packages = PackageSerializer(many=True)

    def create(self, validated_data):
        # TODO
        # - Processar os pacotes recebidos
        # - Persistir informações no banco
        packages = validated_data['packages']
        return Project(name=validated_data['name'])
