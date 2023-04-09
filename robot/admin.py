from django.contrib import admin

from .models import TelegramUser, Movie, Serial, TgUser


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'user', 'id']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'code', 'has_oscar', 'year']
    search_fields = ['title', 'code']

class TgUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'firstname']
    search_fields = ['id', 'username']


# admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Serial, MovieAdmin)
admin.site.register(TgUser, TgUserAdmin)
