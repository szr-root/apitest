from django.db import models

# Create your models here.
from TestTask.models import TestTask
from Testproject.models import TestProject, TestEnv


class CronJob(models.Model):
    """定时任务表"""
    project = models.ForeignKey(TestProject, on_delete=models.CASCADE, help_text='所属项目', verbose_name='所属项目')
    env = models.ForeignKey(TestEnv, help_text='执行环境', verbose_name='执行环境', on_delete=models.PROTECT)
    task = models.ForeignKey(TestTask, help_text='执行任务', verbose_name='执行任务', on_delete=models.PROTECT)
    create_time = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', auto_now_add=True)
    name = models.CharField(max_length=150, help_text='任务名称', verbose_name='任务名称')
    rule = models.CharField(help_text='定时执行规则', verbose_name='定时任务', max_length=80)
    status = models.BooleanField(verbose_name='状态', default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CronJob'
        verbose_name_plural = "定时任务表"
