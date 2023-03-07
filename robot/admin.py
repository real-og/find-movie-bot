from django.contrib import admin

from .models import TelegramUser, Movie, Serial, TgUser


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'user', 'id']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'code', 'has_oscar', 'year']


# admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Serial, MovieAdmin)
admin.site.register(TgUser)
