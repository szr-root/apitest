# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/03
# @File : serializer.py

from rest_framework import serializers
from .models import TestInterface, InterFaceCase


class TestInterfaceSerializer(serializers.ModelSerializer):
    """接口管理的模型序列化器"""

    class Meta:
        model = TestInterface
        fields = "__all__"


class InterFaceCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterFaceCase
        fields = "__all__"


class InterFaceCaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterFaceCase
        fields = ('id', 'title')
