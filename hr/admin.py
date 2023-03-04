from django.contrib import admin

from.models import * 


# Register your models here.
class reg_emailadmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    list_per_page = 10

admin.site.register(Reg_email,reg_emailadmin)

