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
from users.views import LoginView

from rest_framework import routers
from Testproject.views import TestProjectView, TestEnvView, TestFileView
from TestInterface.views import TestInterfaceView,InterFaceCaseView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/users/login/', TokenObtainPairView.as_view(), name='login'),  # 登录
    path('api/users/login/', LoginView.as_view(), name='login'),  # 登录
    path('api/users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
]

router = routers.SimpleRouter()

# 测试项目
router.register(r'api/testPro/projects', TestProjectView)
router.register(r'api/testPro/envs', TestEnvView)
router.register(r'api/testPro/files', TestFileView)

# 测试接口
router.register(r'api/TestInterface/interfaces', TestInterfaceView)
router.register(r'api/TestInterface/cases', InterFaceCaseView)

urlpatterns += router.urls
