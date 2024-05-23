from django.contrib import admin
from . import models


@admin.register(models.Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('file', 'source_year', 'source_number',
                    'created_at', 'updated_at')
    search_fields = ('source_number', 'source_year')
    list_filter = ('created_at', 'updated_at')


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'mediaImage', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('sender', 'message', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('sender',)
    search_fields = ('message',)


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('content', 'journal_image', 'author_image', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('content', 'journal_image', 'author_image')

@admin.register(models.SendingArticle)
class SendingArticleAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('content',)

@admin.register(models.Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('image', 'content', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('image', 'content')
    list_display_links = ('content','created_at', 'updated_at')


@admin.register(models.SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'updated_at')


