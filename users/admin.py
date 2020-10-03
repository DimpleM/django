from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','image_tag')
    search_fields = ('user__username',)
    readonly_fields = ('image_tag',)
    list_filter = ("perAddress__city","gender")

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Address)
