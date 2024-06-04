from ApiTestEngine.core.cases import run_test
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, permissions
from rest_framework.response import Response

from Testproject.models import TestEnv
from .serializer import TestInterfaceSerializer, InterFaceCaseSerializer, InterFaceCaseListSerializer, \
    InterFaceCaseGetSerializer, TestInterfaceListSerializer
from .models import TestInterface, InterFaceCase
from rest_framework.viewsets import ModelViewSet, GenericViewSet


# 接口
class TestInterfaceView(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = TestInterface.objects.all()
    serializer_class = TestInterfaceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('project',)

    def get_serializer_class(self):
        """获取序列化器的方法"""
        if self.action == "list":
            return TestInterfaceListSerializer
        else:
            return self.serializer_class


# 接口用例管理视图
class InterFaceCaseView(ModelViewSet):
    queryset = InterFaceCase.objects.all()
    # serializer_class = InterFaceCaseSerializer
    serializer_class = InterFaceCaseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ("interface",)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = InterFaceCaseListSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     """获取单条用例详情方法"""
    #     instance = self.get_object()
    #     serializer = InterFaceCaseGetSerializer(instance)
    #     return Response(serializer.data)

    # 实现效果等同于下
    def get_serializer_class(self):
        """获取序列化器的方法"""
        if self.action == "list":
            return InterFaceCaseListSerializer
        elif self.action == "retrieve":
            return InterFaceCaseGetSerializer
        else:
            return self.serializer_class

    def run_cases(self, request):
        """运行测试用例"""
        # 获取前段传过来的接口参数
        env_id = request.data.get('env')
        cases = request.data.get('cases')
        if not all([env_id, cases]):
            return Response({'error': 'env和cases不能为空'}, status=400)
        # 获取运行测试环境数据，组长成测试执行引擎所需要的格式
        env = TestEnv.objects.get(id=env_id)

        env_config = {
            "ENV": {
                "host": env.host,
                "headers": env.headers,
                **env.global_variable,
                **env.debug_global_variable,
            },
            "DB": env.db,
            "global_func": env.global_func
        }

        # 获取用例数据，组装
        cases_datas = [
            {
                "name": "调试运行",
                "Cases": [cases]
            }
        ]

        # 调用引擎的run_test方法
        result, ENV = run_test(case_data=cases_datas, env_config=env_config, debug=True)
        # 将运行的环境变量保存到测试环境debug_global_variable中
        env.debug_global_variable = ENV
        env.save()


        return Response(result['results'][0]['cases'][0])
