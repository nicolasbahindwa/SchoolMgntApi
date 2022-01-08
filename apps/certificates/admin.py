from django.contrib import admin
from .models import Certifacate


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_field = ('name', )
 

admin.site.register(Certifacate, CertificateAdmin)
