# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/03
# @File : serializer.py

from rest_framework import serializers
from .models import TestInterface, InterFaceCase


class TestInterfaceSerializer(serializers.ModelSerializer):
    """单条接口管理的模型序列化器"""

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


class InterFaceCaseGetSerializer(serializers.ModelSerializer):
    """获取单条接口详情"""
    interface = TestInterfaceSerializer()

    class Meta:
        model = InterFaceCase
        fields = "__all__"


class TestInterfaceListSerializer(serializers.ModelSerializer):
    """获取接口管理列表的模型序列化器"""
    cases = InterFaceCaseListSerializer(many=True, read_only=True, source='interfacecase_set')

    class Meta:
        model = TestInterface
        fields = "__all__"
