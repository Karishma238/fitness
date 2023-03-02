from django.contrib import admin
from Adminapp.models import Register, SignupInfo, WorkoutSubcategory, WorkoutCategory

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Location', 'Message')


class SignupInfoAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Email', 'Password', 'Mobile')


class WorkoutSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('Lifting_Name', 'Image', 'Description', 'Category')


class WorkoutCategoryAdmin(admin.ModelAdmin):
    list_display = ('Cat_Image', 'Cat_Logo', 'Cat_Name', 'Cat_Description')


admin.site.register(Register, RegisterAdmin)
admin.site.register(SignupInfo, SignupInfoAdmin)
admin.site.register(WorkoutSubcategory, WorkoutSubcategoryAdmin)
admin.site.register(WorkoutCategory, WorkoutCategoryAdmin)
