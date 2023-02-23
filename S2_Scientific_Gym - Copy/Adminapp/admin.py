from django.contrib import admin
from Adminapp.models import Register

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Location', 'Message')


admin.site.register(Register, RegisterAdmin)
