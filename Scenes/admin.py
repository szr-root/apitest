from django.contrib import admin
from .models import TestScenes, SceneToCase


@admin.register(TestScenes)
class TestScentAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name']


@admin.register(SceneToCase)
class SceneToCaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'icase', 'scene', 'sort']
