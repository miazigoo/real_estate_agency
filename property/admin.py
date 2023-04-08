from django.contrib import admin

from .models import Flat


class FlatAdmin (admin.ModelAdmin):
    list_display = ['town', 'owner', 'address']
    list_filter = ['town', ]
    search_fields = ['town', 'owner', 'address']

    class Meta:
        model = Flat


admin.site.register(Flat, FlatAdmin)

