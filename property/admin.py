from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin (admin.ModelAdmin):
    list_display = ['town', 'owner', 'address']
    list_filter = ['town', ]
    search_fields = ['town', 'owner', 'address']
    readonly_fields = ['created_at']

    class Meta:
        model = Flat

