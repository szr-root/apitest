"""ApiTestPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Scenes.views import TestScenesView, SceneToCaseView, UpdateSceneCaseOrder
from TestTask.views import TestTaskView, TestReportView, TestRecordView
from users.views import LoginView

from rest_framework import routers
from Testproject.views import TestProjectView, TestEnvView, TestFileView
from TestInterface.views import TestInterfaceView, InterFaceCaseView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/users/login/', TokenObtainPairView.as_view(), name='login'),  # 登录
    path('api/users/login/', LoginView.as_view(), name='login'),  # 登录
    path('api/users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # 修改测试流程用例顺序
    path('api/testFlow/icases/order/', UpdateSceneCaseOrder.as_view(), name='updateorder'),
    # 运行单条测试用例
    path('api/TestInterFace/cases/run/', InterFaceCaseView.as_view({"post": "run_cases"}), name='run_case'),

    # 运行测试业务流
    path('api/testFlow/scenes/run/', TestScenesView.as_view({
        "post": "run_scene"
    }), name='run_scene'),
    # 运行测试任务
    path('api/TestTask/task/run/', TestTaskView.as_view({
        "post": "run_task"
    }), name='run_task'),

]

router = routers.SimpleRouter()

# 测试项目
router.register(r'api/testPro/projects', TestProjectView)
router.register(r'api/testPro/envs', TestEnvView)
router.register(r'api/testPro/files', TestFileView)

# 测试接口
router.register(r'api/TestInterface/interfaces', TestInterfaceView)
router.register(r'api/TestInterface/cases', InterFaceCaseView)

# 业务流
router.register('api/testFlow/scenes', TestScenesView)

# 业务流用例执行步骤
router.register('api/testFlow/icases', SceneToCaseView)

# 测试任务路由
router.register('api/testTask/tasks', TestTaskView)

# 注册测试报告的路由
router.register('api/testTask/report', TestReportView)
# 注册测试运行记录的路由
router.register('api/testTask/records', TestRecordView)

urlpatterns += router.urls
