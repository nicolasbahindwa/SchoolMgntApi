from django.contrib import admin
from .models import Waitlist


class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'created_at', )
    search_field = ('first_name', 'last_name', )
 

admin.site.register(Waitlist, WaitlistAdmin)
