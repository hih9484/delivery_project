from django.contrib import admin
from board_app.models import BoardDB
# Register your models here.

class BoardDBAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

admin.site.register(BoardDB, BoardDBAdmin)
