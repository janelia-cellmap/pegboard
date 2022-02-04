from django.contrib import admin

from .models import Record, Tissue, Crop

class RecordAdmin(admin.ModelAdmin):
    list_display = ('tissue', 'created', 'last_updated', 'crop')

admin.site.register(Record, RecordAdmin)
admin.site.register(Tissue)
admin.site.register(Crop)
