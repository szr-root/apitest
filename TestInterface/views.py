from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, permissions
from rest_framework.response import Response

from .serializer import TestInterfaceSerializer, InterFaceCaseSerializer,InterFaceCaseListSerializer
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


# 接口用例管理试图
class InterFaceCaseView(ModelViewSet):
    queryset = InterFaceCase.objects.all()
    # serializer_class = InterFaceCaseSerializer
    serializer_class = InterFaceCaseListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ("interface",)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
