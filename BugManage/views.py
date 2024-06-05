from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import BugManage
from .serializer import BugManageSerializer
from rest_framework import permissions


class BugManageView(ModelViewSet):
    queryset = BugManage.objects.all()
    serializer_class = BugManageSerializer
    permission_classes = [permissions.IsAuthenticated]



