from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['town', 'owner', 'address',
                    'new_building', 'price',
                    'construction_year',
                    'owner_pure_phone']
    list_editable = ['new_building', 'price']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']
    search_fields = ['town', 'owner', 'address', 'owner_pure_phone']
    readonly_fields = ['created_at']
    raw_id_fields = ('liked_by',)

    class Meta:
        model = Flat


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'complaint_the_apartment')
    list_display = ['user', 'complaint_the_apartment']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('apartments_in_the_property',)
    list_display = ['owner', 'owner_pure_phone']

