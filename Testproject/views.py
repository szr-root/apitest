import json
import os.path

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from ApiTestPlatform import settings
from Testproject.models import TestProject, TestEnv, TestFile
from .serializer import TestProjectSerializer, TestEnvSerializer, TestFileSerializer
from rest_framework import permissions, mixins

from django_filters import rest_framework as filters


# Project
class TestProjectView(ModelViewSet):
    queryset = TestProject.objects.all()
    serializer_class = TestProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


# Env
class TestEnvView(ModelViewSet):
    queryset = TestEnv.objects.all()
    serializer_class = TestEnvSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('project',)


# TestFile
class TestFileView(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = TestFile.objects.all()
    serializer_class = TestFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """ 重写文件上传方法 1.大小<300kb  2.不能重上传 """
        # 获取上传的文件
        size = request.data['file'].size
        name = request.data['file'].name
        if size > 1024 * 300:
            return Response({"error": "文件大小不能超过300kb"}, status=400)

        if os.path.isfile(settings.MEDIA_ROOT / name):
            return Response({"error": "文件已存在"}, status=400)

        file_type = request.data['file'].content_type
        # 修改info字段值
        request.data['info'] = json.dumps([name, f'files/{name}', file_type])

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """重写删除方法，把保存的文件一起删除"""
        # 删除本地文件
        file_path = self.get_object().info[1]
        os.remove(file_path)

        # 调用父类方法删除
        result = super().destroy(request, *args, **kwargs)
        return result
