from django.contrib import admin

# Register your models here.
from .models import BugManage, BugHandle


@admin.register(BugManage)
class BugManageAdmin(admin.ModelAdmin):
    list_display = ['create_time', 'interface', 'desc', 'status', 'user']


@admin.register(BugHandle)
class BugHandleAdmin(admin.ModelAdmin):
    list_display = ['bug', 'create_time', 'handle', 'update_user']
