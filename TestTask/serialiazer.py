# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/04
# @File : serialiazer.py
from Scenes.serializer import TestSceneSerializer
from .models import TestTask, TestRecord, TestReport
from rest_framework import serializers


class TestTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTask
        fields = "__all__"


class TestTaskGetSerializer(serializers.ModelSerializer):
    scene = TestSceneSerializer(many=True)

    class Meta:
        model = TestTask
        fields = "__all__"


class TestRecordSerializer(serializers.ModelSerializer):
    env = serializers.StringRelatedField(read_only=True, source='env')
    task = serializers.StringRelatedField(read_only=True, source='task')

    class Meta:
        model = TestRecord
        fields = "__all__"


class TestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestReport
        fields = "__all__"
