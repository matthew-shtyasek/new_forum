from django.contrib import admin
from platform_.models import *


@admin.register(Partition)
class PartitionAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['name', 'visible']
    list_editable = ['visible']
    search_fields = ['name']
    list_filter = ['visible']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['name', 'partition', 'visible']
    list_editable = ['visible']
    search_fields = ['name']
    list_filter = ['visible', 'partition']


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['name',
                    'category',
                    'author',
                    'visible']
    list_editable = ['visible']
    search_fields = ['name',
                     'author__username']
    list_filter = ['visible',
                   'category']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['author',
                    'theme',
                    'send_date',
                    'edit_date',
                    'visible']
    list_editable = ['visible']
    search_fields = ['name',
                     'body']
    list_filter = ['visible',
                   'theme',
                   'send_date',
                   'edit_date']
    readonly_fields = ['send_date',
                       'edit_date']


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['image',
                    'post',
                    'visible']
    list_editable = ['visible']
    list_filter = ['post',
                   'visible']
