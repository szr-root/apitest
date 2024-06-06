from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import BugManage, BugHandle
from .serializer import BugManageSerializer, BugManageListSerializer
from rest_framework import permissions, mixins


class BugManageView(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = BugManage.objects.all()
    serializer_class = BugManageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return BugManageListSerializer
        else:
            return self.serializer_class

    def create(self, request, *args, **kwargs):
        result = super().create(request, *args, **kwargs)

        bug = BugManage.objects.get(id=result.data.get('id'))
        handler_info = f"提交bug，状态是{result.data.get('status')}"
        # 新增一条bug记录
        BugHandle.objects.create(bug=bug, handle=handler_info, update_user=request.user.username)
        return result

    def update(self, request, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        bug = self.get_object()
        # 新增一条bug处理记录
        handler_info = f"提交bug，状态是{result.data.get('status')}"
        # 新增一条bug记录
        BugHandle.objects.create(bug=bug, handle=handler_info, update_user=request.user.username)

        return result
