# Generated by Django 5.0.6 on 2024-06-03 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestInterface', '0002_intercase'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InterCase',
            new_name='InterFaceCase',
        ),
        migrations.AlterModelOptions(
            name='interfacecase',
            options={'verbose_name_plural': '接口用例表'},
        ),
    ]
