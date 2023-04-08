from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['town', 'owner', 'address',
                    'new_building', 'price',
                    'construction_year']
    list_editable = ['new_building', 'price']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']
    search_fields = ['town', 'owner', 'address']
    readonly_fields = ['created_at']

    class Meta:
        model = Flat


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'complaint_the_apartment')
    list_display = ['user', 'complaint_the_apartment']

