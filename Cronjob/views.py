import json

from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, mixins
from rest_framework.response import Response

from .models import CronJob

from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .serializer import CronJobSerializer

from django_celery_beat.models import CrontabSchedule, PeriodicTask

from django.db import transaction


class CronJobView(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = CronJob.objects.all()
    serializer_class = CronJobSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project', 'task']

    def create(self, request, *args, **kwargs):
        """创建定时任务"""
        # 开启事务
        with transaction.atomic():
            # 创建事务保存节点
            save_point = transaction.savepoint()
            try:
                result = super().create(request, *args, **kwargs)
                # 获取定时任务规则
                rule = result.data.get('rule').split(" ")
                rule_dict = dict(zip(['minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year'], rule))
                # CrontabSchedule创建规则对象
                try:
                    cron = CrontabSchedule.objects.get(**rule_dict)
                except:
                    cron = CrontabSchedule.objects.create(**rule_dict)

                # PeriodicTask创建周期性调度
                PeriodicTask.objects.create(
                    name=result.data.get('id'),
                    task='TestTask.tasks.run_test_task',
                    crontab=cron,
                    kwargs=json.dumps({
                        'env_id': result.data.get('env'),
                        'task_id': result.data.get('task'),
                        'tester': request.user.username
                    }),
                    enabled=result.data.get('status')
                )
            except:
                # 事务回滚
                transaction.savepoint_rollback(save_point)
                return Response({"error": "创建定时任务失败"}, status=500)
            else:
                # 提交事务
                transaction.savepoint_commit(save_point)
                return result

    def update(self, request, *args, **kwargs):
        save_point = transaction.savepoint()
        try:
            # 调用父类方法更新数据
            res = super().update(request, *args, **kwargs)
            cronjob = self.get_object()
            # 更新周期任务和时间规则
            ptask = PeriodicTask.objects.get(name=res.data.get('id'))
            ptask.kwargs = json.dumps({
                'env_id': res.data.get('env'),
                'task_id': res.data.get('task'),
            }),
            ptask.enabled = res.data.status
            # 获取执行规则
            rule = res.data.get('rule').split(" ")
            rule_dict = dict(zip(['minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year'], rule))
            # CrontabSchedule创建规则对象
            try:
                cron = CrontabSchedule.objects.get(**rule_dict)
            except:
                cron = CrontabSchedule.objects.create(**rule_dict)

            ptask.crontab = cron
            ptask.save()

        except:
            transaction.savepoint_rollback(save_point)
            return Response({"error": "修改失败！"})
        else:
            transaction.savepoint_commit(save_point)
            return res

    def destroy(self, request, *args, **kwargs):
        save_point = transaction.savepoint()
        try:
            cronjob = self.get_object()
            ptask = PeriodicTask.objects.get(id=cronjob.id)
            ptask.enabled = False
            ptask.delete()
            res = super().destroy(request, *args, **kwargs)
        except:
            transaction.savepoint_rollback(save_point)
            return Response({"error": "删除失败！"})
        else:
            transaction.savepoint_commit(save_point)
            return res
