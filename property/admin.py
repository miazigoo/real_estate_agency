from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin (admin.ModelAdmin):
    list_display = ['town', 'owner', 'address',
                    'new_building', 'price',
                    'construction_year']
    list_editable = ['new_building', 'price']
    list_filter = ['town', ]
    search_fields = ['town', 'owner', 'address']
    readonly_fields = ['created_at']

    class Meta:
        model = Flat

