from django.db import models

# Create your models here.
from Scenes.models import TestScenes
from Testproject.models import TestProject, TestEnv


class TestTask(models.Model):
    """测试任务的模型类"""
    project = models.ForeignKey(TestProject, on_delete=models.PROTECT, verbose_name="所属项目", help_text='所属项目')
    name = models.CharField(max_length=50, help_text='任务名称', verbose_name='任务名称')
    scene = models.ManyToManyField(TestScenes, blank=True, help_text='包含的业务流', verbose_name='包含的业务流')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'testTask'
        verbose_name_plural = '测试任务表'


class TestRecord(models.Model):
    """测试运行记录"""
    task = models.ForeignKey(TestTask, on_delete=models.CASCADE, verbose_name='测试任务表', help_text='测试任务表')
    env = models.ForeignKey(TestEnv, on_delete=models.PROTECT, verbose_name='执行环境', help_text='执行环境')
    all = models.IntegerField(verbose_name='用例总数', help_text='用例总数', default=0, blank=True)
    success = models.IntegerField(verbose_name='通过用例数', help_text='通过用例数', default=0, blank=True)
    fail = models.IntegerField(verbose_name='失败用例数', help_text='失败用例数', default=0, blank=True)
    error = models.IntegerField(verbose_name='错误用例数', help_text='错误用例数', default=0, blank=True)
    pass_rate = models.CharField(max_length=50, verbose_name='通过率', help_text='通过率', default='0', blank=True)
    tester = models.CharField(max_length=50, verbose_name='执行者', help_text='执行者', blank=True)
    status = models.CharField(max_length=50, verbose_name='执行状态', help_text='执行状态')
    create_time = models.DateTimeField(auto_created=True, verbose_name='执行时间', help_text='执行时间',auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'testRecord'
        verbose_name_plural = '运行记录表'


class TestReport(models.Model):
    info = models.JSONField(verbose_name='报告的数据', help_text='报告的数据', default=dict, blank=True)
    record = models.ForeignKey(TestRecord, on_delete=models.CASCADE, verbose_name='测试记录', help_text='测试记录')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'testReport'
        verbose_name_plural = '测试报告表'
