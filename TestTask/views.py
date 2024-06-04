from ApiTestEngine.core.cases import run_test
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Scenes.serializer import SceneRunSerializer
from TestTask.models import TestTask, TestRecord, TestReport
from TestTask.serialiazer import TestTaskSerializer, TestTaskGetSerializer, TestRecordSerializer, TestReportSerializer
from rest_framework import permissions, mixins

from Testproject.models import TestEnv


class TestTaskView(ModelViewSet):
    """定义测试任务类"""
    queryset = TestTask.objects.all()
    serializer_class = TestTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('project',)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TestTaskGetSerializer
        else:
            return self.serializer_class

    def run_task(self, request):
        """运行测试任务"""
        # 获取参数:env 和scene,校验参数是否为空
        env_id = request.data.get('env')
        task = request.data.get('scene')
        if not all([env_id, task]):
            return Response({'error': "参数env和task均不能为空"}, status=400)

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
        # 获取测试任务中的所有测试业务流
        scenes = TestTask.objects.get(id=task_id).scene.all()

        # 获取业务流中的测试数据
        case_data = []
        for scene in scenes:
            scene_cases = scene.scenetocase_set.all()
            res = SceneRunSerializer(scene_cases, many=True).data
            # 根据sort字段进行排序
            datas = sorted(res, key=lambda x: x['sort'])
            case_data.append({
                "name": scene.name,
                "Cases": [item['icase'] for item in datas]
            })

        record = TestRecord.objects.create(tasks=task.name, env=env.name, tester=request.user.username, status="执行中")

        # 运行测试
        result = run_test(case_data, env_config, debug=False)

        # 保存测试报告
        TestReport.objects.create(info=result, record=record)
        record.all = result.get('all', 0)
        record.success = result.get('success', 0)
        record.fail = result.get('fail', 0)
        record.error = result.get('error', 0)
        record.pass_rate = "{:.2f}".format(100 * result.get('success', 0) / result.get('all', 1)) if result.get('all',
                                                                                                       0) else '0'
        record.statue = '执行完毕'
        record.save()

        return Response(result)


from django_filters.rest_framework import FilterSet
from django_filters import filters


class TestRecordFilterSet(FilterSet):
    """测试记录的过滤器"""
    project = filters.NumberFilter(field_name='task__project')


class Meta:
    model = TestRecord
    # 指定过滤的参数
    fields = ['task', 'project']


class TestRecordView(mixins.ListModelMixin, GenericViewSet):
    queryset = TestRecord.objects.all()
    serializer_class = TestRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    # 没有project字段，需要重写过滤器
    # filterset_fields = ['project','task']


class TestReportView(mixins.ListModelMixin, GenericViewSet):
    queryset = TestReport.objects.all()
    serializer_class = TestReportSerializer
    permission_classes = [permissions.IsAuthenticated]
