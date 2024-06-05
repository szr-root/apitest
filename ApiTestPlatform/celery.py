# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/05
# @File : celery.py

# 创建一个celery应用，并且加载settings中的配置
import os
from celery import Celery

# 1 导入django的配置文件(可以在WSGI中找到)---》后续在celery的任务中，就可以直接使用django的orm，缓存
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ApiTestPlatform.settings')
# 2 实例化得到celery对象
celery_app = Celery('Light')
# 3 celery的配置，使用django 配置文件中的配置--》刚刚写的配置
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# 4 这句话会去所有app中，自动查找 tasks.py 文件，作为任务文件
celery_app.autodiscover_tasks()
