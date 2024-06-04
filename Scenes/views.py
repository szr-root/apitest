from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Scenes.models import TestScenes, SceneToCase
from Scenes.serializer import TestSceneSerializer, SceneToCaseSerializer, SceneToCaseListSerializer, SceneRunSerializer
from Testproject.models import TestEnv


class TestScenesView(ModelViewSet):
    queryset = TestScenes.objects.all()
    serializer_class = TestSceneSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project']


    def run_scene(self,request):
        """运行测试业务流"""
        # 获取参数:env 和scene,校验参数是否为空
        env_id = request.data.get('env')
        scene_id = request.data.get('scene')
        if not all([env_id, scene_id]):
            return Response({'error': "参数env和scene均不能为空"}, status=400)
        # 获取测试环境数据
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
        # 获取测试业务流中的用例数据
        scene = TestScenes.objects.get(id=scene_id)
        scene_cases = scene.scenetocase_set.all()
        res = SceneRunSerializer(scene_cases, many=True).data
        # print(res)
        # 根据sort字段进行排序
        datas = sorted(res, key=lambda x: x['sort'])
        # print(datas)
        cases = []
        for item in datas:
            cases.append(item['icase'])
        # 执行的用例数据
        case_data = [
            {
                "name": scene.name,
                "Cases": cases
            }
        ]
        # print("case_data::::",case_data)
        # 调用执行引擎的run_test方法运行测试
        from ApiTestEngine.core.cases import run_test
        result = run_test(case_data, env_config, debug=False)
        return Response(result['results'][0], status=200)


class SceneToCaseView(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """业务流用例执行顺序"""
    queryset = SceneToCase.objects.all()
    serializer_class = SceneToCaseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['scene']

    def get_serializer_class(self):
        if self.action == "list":
            return SceneToCaseListSerializer
        else:
            return self.serializer_class


class UpdateSceneCaseOrder(APIView):
    def patch(self, request):
        datas = request.data
        for item in datas:
            # 通过id找到执行用例对象，修改sort
            obj = SceneToCase.objects.get(id=item['id'])
            obj.sort = item['sort']
            obj.save()

        return Response({'msa': 'ok', 'data': datas})

        pass
