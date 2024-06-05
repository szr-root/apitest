# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/05
# @File : serializer.py

from rest_framework import serializers
from .models import CronJob


class CronJobSerializer(serializers.ModelSerializer):
    task_name = serializers.StringRelatedField(read_only=True, source='task.name')
    env_name = serializers.StringRelatedField(read_only=True, source='env.name')

    class Meta:
        model = CronJob
        fields = '__all__'
