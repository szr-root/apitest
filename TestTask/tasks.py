# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2024/06/05
# @File : tasks.py
from ApiTestEngine.core.cases import run_test
from rest_framework.response import Response

from ApiTestPlatform.celery import celery_app
from Scenes.serializer import SceneRunSerializer
from TestTask.models import TestTask, TestRecord, TestReport
from Testproject.models import TestEnv


@celery_app.task
def run_test_task(env_id, task_id, tester):
    """

    :param env_id: 环境id
    :param task_id: 任务id
    :param tester: 调用人
    :return:
    """
    env = TestEnv.objects.get(id=env_id)
    env_config = {
        "ENV": {
            "host": env.host,
            "headers": env.headers,
            **env.global_variable,
        },
        "DB": env.db,
        "global_func": env.global_func
    }
    # 获取测试任务
    task = TestTask.objects.get(id=task_id)

    # 获取任务中所有业务流
    scenes = task.scene.all()

    # 获取业务流中的测试数据
    case_data = []
    for scene in scenes:
        cases = scene.scenetocase_set.all()
        res = SceneRunSerializer(cases, many=True).data
        # 根据sort字段进行排序
        datas = sorted(res, key=lambda x: x['sort'])
        case_data.append({
            "name": scene.name,
            "Cases": [item['icase'] for item in datas]
        })

    record = TestRecord.objects.create(task=task, env=env, tester=tester, status="执行中")

    # 运行测试
    result = run_test(case_data, env_config, debug=False)

    # 保存测试报告
    TestReport.objects.create(info=result, record=record)
    record.all = result.get('all', 0)
    record.success = result.get('success', 0)
    record.fail = result.get('fail', 0)
    record.error = result.get('error', 0)
    record.pass_rate = "{:.2f}".format(100 * result.get('success', 0) / result.get('all', 1))
    record.status = '执行完毕'
    record.save()

    return Response(result)


@celery_app.task
def work2():
    print("task ----work2")
