from django.db import models


# Create your models here.


class TestProject(models.Model):
    """项目表"""
    create_time = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', auto_now_add=True)
    name = models.CharField(max_length=50, help_text='项目名称', verbose_name='项目名')
    leader = models.CharField(max_length=50, help_text='负责人', verbose_name='负责人', default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TestProject'
        verbose_name_plural = "测试项目表"


class TestEnv(models.Model):
    """测试环境表"""
    project = models.ForeignKey(to=TestProject, on_delete=models.CASCADE, help_text='所属项目', verbose_name='所属项目')
    global_variable = models.JSONField(help_text='全局变量', verbose_name='全局变量', default=dict, null=True,
                                       blank=True)
    debug_global_variable = models.JSONField(help_text='debug模式全局变量', verbose_name='debug模式全局变量',
                                             default=dict, null=True, blank=True)
    db = models.JSONField(help_text='数据库配置', verbose_name='数据库配置', default=list, null=True, blank=True)
    headers = models.JSONField(help_text='请求头', verbose_name='请求头', default=dict, null=True, blank=True)
    global_func = models.TextField(help_text='用例工具文件', verbose_name='用例工具文件', default="", null=True, blank=True)
    name = models.CharField(max_length=150, help_text='测试环境名称', verbose_name='测试环境名称')
    host = models.CharField(help_text='base_url地址', verbose_name='base_url地址', max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TestEnv'
        verbose_name_plural = "测试环境表"


class TestFile(models.Model):
    """文件上传"""
    file = models.FileField(help_text='文件', verbose_name='文件')
    info = models.JSONField(help_text='数据', verbose_name='数据', default=list, blank=True)

    def __str__(self):
        return self.info

    class Meta:
        db_table = 'TestFile'
        verbose_name_plural = "测试文件表"
