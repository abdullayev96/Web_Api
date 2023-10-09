from django.contrib import admin
from .models import *



class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title']
    search_fields = ['name']


admin.site.register(Childern, ChildrenAdmin)

