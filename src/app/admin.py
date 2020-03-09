from django.contrib import admin

# Register your models here.
from .models import TreeMenu, TreeMenuCategory


@admin.register(TreeMenuCategory)
class TreeMenuCategoryAdmin(admin.ModelAdmin):

    fields = ['name', 'verbose_name', ]
    list_display = ['__str__', ]


@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):

    fields = ['name', 'category', 'path', 'parent', ]
    list_display = ['__str__', 'category', 'path', 'parent', ]

    # filter_horizontal = ['category__name', ]

