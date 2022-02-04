from django.contrib import admin

from .models import Record, Tissue, Crop

class RecordAdmin(admin.ModelAdmin):
    list_display = ('tissue', 'created', 'last_updated', 'crop')
    list_filter = ('tissue', )
    list_select_related = ('tissue', 'crop')
    search_fields = ('tissue__short_name', 'crop__short_name')

admin.site.register(Record, RecordAdmin)
admin.site.register(Tissue)
admin.site.register(Crop)
