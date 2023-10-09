from django.contrib import admin
from .models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'bio', 'number_book']
    search_fields = ['full_name']



class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image', 'author', 'category']
    search_fields = ['author', 'category']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)


