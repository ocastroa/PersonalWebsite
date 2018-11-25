from django.contrib import admin

from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_app', 'app_id', 'date_finished', 'is_published')
    list_display_links = ('id', 'name_of_app')
    list_editable = ('is_published',)
    search_fields = ('name_of_app', 'date_finished')
    list_per_page = 25

admin.site.register(Portfolio, PortfolioAdmin)