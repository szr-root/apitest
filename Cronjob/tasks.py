# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/05
# @File : tasks.py

from ApiTestPlatform.celery import celery_app

@celery_app.task
def work1():
    print("work1")


@celery_app.task
def work2():
    print("work2")