# Generated by Django 5.0.6 on 2024-06-05 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestTask', '0003_alter_testrecord_create_time'),
        ('Testproject', '0002_alter_testenv_name_alter_testenv_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='CronJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('name', models.CharField(help_text='任务名称', max_length=150, verbose_name='任务名称')),
                ('rule', models.CharField(help_text='定时执行规则', max_length=80, verbose_name='定时任务')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
                ('env', models.ForeignKey(help_text='执行环境', on_delete=django.db.models.deletion.PROTECT, to='Testproject.testenv', verbose_name='执行环境')),
                ('project', models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.CASCADE, to='Testproject.testproject', verbose_name='所属项目')),
                ('task', models.ForeignKey(help_text='执行任务', on_delete=django.db.models.deletion.PROTECT, to='TestTask.testtask', verbose_name='执行任务')),
            ],
            options={
                'verbose_name_plural': '定时任务表',
                'db_table': 'CronJob',
            },
        ),
    ]