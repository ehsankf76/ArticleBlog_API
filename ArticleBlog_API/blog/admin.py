from django.contrib import admin

from . import models



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'last_update')
    list_filter = ('create_time', 'last_update')
    search_fields = ('title', 'author', 'category')

admin.site.register(models.Category)
admin.site.register(models.Article, ArticleAdmin)