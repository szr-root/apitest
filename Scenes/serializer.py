# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/04
# @File : serializer.py

from rest_framework import serializers

from Scenes.models import TestScenes, SceneToCase

from TestInterface.serializer import InterFaceCaseListSerializer, InterFaceCaseGetSerializer


class TestSceneSerializer(serializers.ModelSerializer):
    """测试业务流中序列化器"""

    class Meta:
        model = TestScenes
        fields = '__all__'


class SceneToCaseSerializer(serializers.ModelSerializer):
    """测试业务流中的测试用例执行步骤"""

    class Meta:
        model = SceneToCase
        fields = '__all__'


class SceneToCaseListSerializer(serializers.ModelSerializer):
    """获取列表"""
    icase = InterFaceCaseListSerializer()

    # scene = TestSceneSerializer()

    class Meta:
        model = SceneToCase
        fields = '__all__'


class SceneRunSerializer(serializers.ModelSerializer):
    icase = InterFaceCaseGetSerializer()

    class Meta:
        model = SceneToCase
        fields = '__all__'
