# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/05
# @File : serializer.py

from .models import BugHandle, BugManage
from rest_framework import serializers


class BugHandleSerializer(serializers.ModelSerializer):
    """bug处理记录的序列化器"""

    class Meta:
        model = BugHandle
        fields = '__all__'


class BugManageSerializer(serializers.ModelSerializer):
    """bug管理的序列化器"""
    interface_url = serializers.StringRelatedField(source='interface.url', read_only=True)
    handle = BugHandleSerializer(many=True, source="bughandle_set", read_only=True)

    class Meta:
        model = BugManage
        fields = '__all__'
        # exclude = ['create_time', 'interface']


class BugManageListSerializer(serializers.ModelSerializer):
    interface_url = serializers.StringRelatedField(source='interface.url', read_only=True)

    class Meta:
        model = BugManage
        fields = ['id', 'desc', 'interface_url', 'status', 'user', 'create_time']
