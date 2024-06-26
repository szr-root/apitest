# Generated by Django 5.0.6 on 2024-06-04 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestTask', '0001_initial'),
        ('Testproject', '0002_alter_testenv_name_alter_testenv_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, help_text='执行时间', verbose_name='执行时间')),
                ('all', models.IntegerField(blank=True, default=0, help_text='用例总数', verbose_name='用例总数')),
                ('success', models.IntegerField(blank=True, default=0, help_text='通过用例数', verbose_name='通过用例数')),
                ('fail', models.IntegerField(blank=True, default=0, help_text='失败用例数', verbose_name='失败用例数')),
                ('error', models.IntegerField(blank=True, default=0, help_text='错误用例数', verbose_name='错误用例数')),
                ('pass_rate', models.CharField(blank=True, default='0', help_text='通过率', max_length=50, verbose_name='通过率')),
                ('tester', models.CharField(blank=True, help_text='执行者', max_length=50, verbose_name='执行者')),
                ('status', models.CharField(help_text='执行状态', max_length=50, verbose_name='执行状态')),
                ('env', models.ForeignKey(help_text='执行环境', on_delete=django.db.models.deletion.PROTECT, to='Testproject.testenv', verbose_name='执行环境')),
                ('task', models.ForeignKey(help_text='测试任务表', on_delete=django.db.models.deletion.CASCADE, to='TestTask.testtask', verbose_name='测试任务表')),
            ],
            options={
                'verbose_name_plural': '运行记录表',
                'db_table': 'testRecord',
            },
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.JSONField(blank=True, default=dict, help_text='报告的数据', verbose_name='报告的数据')),
                ('record', models.ForeignKey(help_text='测试记录', on_delete=django.db.models.deletion.CASCADE, to='TestTask.testrecord', verbose_name='测试记录')),
            ],
            options={
                'verbose_name_plural': '测试报告表',
                'db_table': 'testReport',
            },
        ),
    ]
