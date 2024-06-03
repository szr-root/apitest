from django.db import models
from Testproject.models import TestProject


# Create your models here.

# 接口管理
class TestInterface(models.Model):
    """接口表"""
    CHOICES = [
        ('1', '项目接口'),
        ('2', '外部接口')
    ]
    project = models.ForeignKey(TestProject, on_delete=models.CASCADE, help_text='项目id', verbose_name='项目id')
    name = models.CharField(max_length=50, help_text='接口名称', verbose_name='接口名')
    url = models.CharField(max_length=200, help_text='接口路径', verbose_name='接口路径')
    method = models.CharField(max_length=50, help_text='请求方法', verbose_name='请求方法')
    type = models.CharField(verbose_name='接口类型', help_text='接口类型', max_length=40, choices=CHOICES, default='1')

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'interface'
        verbose_name_plural = "接口表"


# 接口用例管理
class InterFaceCase(models.Model):
    """接口用例管理"""
    title = models.CharField(verbose_name='用例名称', help_text='用例名称', max_length=50)
    interface = models.ForeignKey(to=TestInterface, on_delete=models.CASCADE, verbose_name='接口', help_text='接口')
    headers = models.JSONField(verbose_name='请求头配置', help_text='请求头', null=True, default=dict, blank=True)
    request = models.JSONField(verbose_name='请求参数配置', help_text='请求参数配置', null=True, default=dict,
                               blank=True)
    file = models.JSONField(verbose_name='请求上传的文件参数', help_text='请求上传的文件参数', null=True, default=list,
                            blank=True)
    setup_script = models.TextField(verbose_name='前置脚本', help_text='前置脚本', null=True, blank=True, default='')
    teardown_script = models.TextField(verbose_name='后置脚本', help_text='后置脚本', null=True, blank=True, default='')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'interFaceCases'
        verbose_name_plural = "接口用例表"
