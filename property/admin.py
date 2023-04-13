from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.apartments.through
    raw_id_fields = ('flat', 'owner')
    extra = 0


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [OwnerInline]
    list_display = ['town', 'address',
                    'new_building', 'price',
                    'construction_year']
    list_editable = ['new_building', 'price']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    raw_id_fields = ('liked_by',)

    class Meta:
        model = Flat


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'apartment')
    list_display = ['user', 'apartment']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('apartments',)
    list_display = ['full_name', 'pure_phone']
    inlines = [OwnerInline]

