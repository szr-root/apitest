from django.db import models

# Create your models here.
from TestInterface.models import TestInterface


class BugManage(models.Model):
    """bug管理的模型类"""
    interface = models.ForeignKey(TestInterface, on_delete=models.CASCADE, verbose_name="所属接口",
                                  help_text="所属接口")
    create_time = models.DateTimeField(auto_now_add=True, help_text="提交时间", verbose_name="提交时间")
    desc = models.CharField(max_length=30, verbose_name="bug描述", help_text="bug描述", blank=True)
    # bug状态：处理中、未处理、已关闭、无效bug
    status = models.CharField(max_length=10, help_text="bug状态", verbose_name="bug状态")
    user = models.CharField(max_length=10, help_text="提交者", verbose_name="提交者", blank=True)
    info = models.JSONField(help_text="用例执行信息", verbose_name='用例执行信息', default=dict, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'bugmanage'
        verbose_name_plural = 'bug管理表'


class BugHandle(models.Model):
    """bug处理记录表"""
    bug = models.ForeignKey(BugManage, on_delete=models.CASCADE, help_text='bug', verbose_name='bug')
    create_time = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', auto_now_add=True)
    handle = models.TextField(help_text='处理操作', verbose_name='处理操作', blank=True)
    update_user = models.CharField(max_length=32, verbose_name='更新用户', help_text='更新用户', blank=True)

    class Meta:
        db_table = 'bughandle'
        verbose_name_plural = "bug操作记录表"
