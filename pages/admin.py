from django.contrib import admin

from .models import Pages

class PagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Pages, PagesAdmin)