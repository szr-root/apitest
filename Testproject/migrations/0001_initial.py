# Generated by Django 4.1 on 2024-06-03 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='文件', upload_to='', verbose_name='文件')),
                ('info', models.JSONField(blank=True, default=list, help_text='数据', verbose_name='数据')),
            ],
            options={
                'verbose_name_plural': '测试文件表',
                'db_table': 'TestFile',
            },
        ),
        migrations.CreateModel(
            name='TestProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('name', models.CharField(help_text='项目名称', max_length=50, verbose_name='项目名')),
                ('leader', models.CharField(default='', help_text='负责人', max_length=50, verbose_name='负责人')),
            ],
            options={
                'verbose_name_plural': '测试项目表',
                'db_table': 'TestProject',
            },
        ),
        migrations.CreateModel(
            name='TestEnv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='环境名称', max_length=150, verbose_name='环境名称')),
                ('global_variable', models.JSONField(blank=True, default=dict, help_text='全局变量', null=True, verbose_name='全局变量')),
                ('debug_global_variable', models.JSONField(blank=True, default=dict, help_text='debug模式全局变量', null=True, verbose_name='debug模式全局变量')),
                ('db', models.JSONField(blank=True, default=list, help_text='数据库配置', null=True, verbose_name='数据库配置')),
                ('host', models.CharField(blank=True, help_text='base_url地址', max_length=100, verbose_name='base_url地址')),
                ('headers', models.JSONField(blank=True, default=dict, help_text='请求头', null=True, verbose_name='请求头')),
                ('global_func', models.TextField(blank=True, default='', help_text='用例工具文件', null=True, verbose_name='用例工具文件')),
                ('project', models.ForeignKey(help_text='项目id', on_delete=django.db.models.deletion.CASCADE, to='Testproject.testproject', verbose_name='项目id')),
            ],
            options={
                'verbose_name_plural': '测试环境表',
                'db_table': 'TestEnv',
            },
        ),
    ]
