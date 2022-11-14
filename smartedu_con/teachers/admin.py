from django.contrib import admin
from . models import Teachers

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)