# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/03
# @File : serializer.py
from rest_framework import serializers
from .models import TestProject, TestEnv, TestFile


class TestProjectSerializer(serializers.ModelSerializer):
    """序列化器"""

    class Meta:
        model = TestProject
        fields = "__all__"


class TestEnvSerializer(serializers.ModelSerializer):
    """测试环境序列化器"""

    class Meta:
        model = TestEnv
        fields = '__all__'


class TestFileSerializer(serializers.ModelSerializer):
    """文件上传序列化器"""

    class Meta:
        model = TestFile
        fields = '__all__'
