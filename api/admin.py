from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
   list_display = ('first_name', 'last_name', 'age','address','gender')
   search_fields = ('first_name', 'last_name')
admin.site.register(Patient, PatientAdmin)
