# Generated by Django 5.0.6 on 2024-06-04 02:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Testproject', '0002_alter_testenv_name_alter_testenv_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestScent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='测试业务流名', max_length=50, verbose_name='测试业务流名')),
                ('project', models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.PROTECT, to='Testproject.testproject', verbose_name='项目名称')),
            ],
            options={
                'verbose_name_plural': '测试业务流',
                'db_table': 'test_scent',
            },
        ),
    ]
