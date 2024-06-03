from django.contrib import admin

# Register your models here.
from TestInterface.models import TestInterface, InterFaceCase


@admin.register(TestInterface)
class TestInterfaceAdmin(admin.ModelAdmin):
    list_display = ["id", "project", "name", "method", "url", "type"]


@admin.register(InterFaceCase)
class InterCaseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "interface"]
