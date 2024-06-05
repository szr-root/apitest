from ApiTestEngine.core.cases import run_test
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Scenes.serializer import SceneRunSerializer
from TestTask.models import TestTask, TestRecord, TestReport
from TestTask.serialiazer import TestTaskSerializer, TestTaskGetSerializer, TestRecordSerializer, TestReportSerializer
from rest_framework import permissions, mixins
from .tasks import run_test_task

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
        task_id = request.data.get('task')
        if not all([env_id, task_id]):
            return Response({'error': "参数env和task均不能为空"}, status=400)

        # 异步执行任务
        run_test_task.delay(env_id, task_id, request.user.username)
        return Response({"msg": "测试任务开始执行！"}, status=200)


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
    queryset = TestRecord.objects.all().order_by('-create_time')
    serializer_class = TestRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    # 没有project字段，需要重写过滤器
    # filterset_fields = ['project','task']


class TestReportView(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = TestReport.objects.all()
    serializer_class = TestReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        # instance = self.get_object()
        test_record = TestRecord.objects.get(id=kwargs['pk'])
        test_report = TestReport.objects.get(record=test_record)

        serializer = self.get_serializer(test_report)
        return Response(serializer.data)
