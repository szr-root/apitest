# Generated by Django 5.0.6 on 2024-06-03 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Testproject', '0002_alter_testenv_name_alter_testenv_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestInterface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='接口名称', max_length=50, verbose_name='接口名')),
                ('url', models.CharField(help_text='接口路径', max_length=200, verbose_name='接口路径')),
                ('method', models.CharField(help_text='请求方法', max_length=50, verbose_name='请求方法')),
                ('type', models.CharField(choices=[('1', '项目接口'), ('2', '外部接口')], default='1', help_text='接口类型', max_length=40, verbose_name='接口类型')),
                ('project', models.ForeignKey(help_text='项目id', on_delete=django.db.models.deletion.CASCADE, to='Testproject.testproject', verbose_name='项目id')),
            ],
            options={
                'verbose_name_plural': '接口表',
                'db_table': 'interface',
            },
        ),
    ]
