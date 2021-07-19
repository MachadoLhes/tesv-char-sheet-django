from django.contrib import admin
from .models import *

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name','race','sex')
    ordering = ('name',)
    search_fields = ('name',)