from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.category.models import Category
from rest_framework import  permissions

from apps.category.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            return [permissions.AllowAny(),]
        return [permissions.IsAdminUser(),]

