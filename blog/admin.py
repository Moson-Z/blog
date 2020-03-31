from django.contrib import admin

from django.contrib import admin
from .models import Article, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tag']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'num']
#     fields = ['name']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)

