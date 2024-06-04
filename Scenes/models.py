from django.db import models

# Create your models here.
from TestInterface.models import InterFaceCase
from Testproject.models import TestProject


class TestScenes(models.Model):
    """测试业务流"""
    project = models.ForeignKey(TestProject, help_text='所属项目', verbose_name='项目名称', on_delete=models.PROTECT)
    name = models.CharField(max_length=50, help_text='测试业务流名', verbose_name='测试业务流名')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_scent'
        verbose_name_plural = "测试业务流"


class SceneToCase(models.Model):
    icase = models.ForeignKey(InterFaceCase, on_delete=models.PROTECT, verbose_name='接口用例', help_text='接口用例')
    scene = models.ForeignKey(TestScenes, on_delete=models.PROTECT, verbose_name='测试业务流', help_text='测试业务流')
    sort = models.IntegerField(verbose_name='执行顺序', help_text='执行顺序', null=True, blank=True)

    def __str__(self):
        return self.icase.title

    class Meta:
        verbose_name_plural = '测试业务流中的执行步骤'