from django.contrib import admin

# Register your models here.
from Cronjob.models import CronJob


@admin.register(CronJob)
class CronJobAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_time', 'name', 'env', 'task', 'status', 'rule']

