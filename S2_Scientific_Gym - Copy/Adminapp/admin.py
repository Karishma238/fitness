from django.contrib import admin
from Adminapp.models import Register, SignupInfo, WorkoutExercise, WorkoutCategory, WorkoutSubcategory, Packages

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Location', 'Message')


class SignupInfoAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Email', 'Password', 'Mobile')


class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('Exer_Name', 'Image', 'Description', 'Category')


class WorkoutSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('Lifting_Name', 'Image', 'Description')


class WorkoutCategoryAdmin(admin.ModelAdmin):
    list_display = ( 'Cat_Name', 'Cat_Image', 'Cat_Logo','Cat_Description')


class PackagesAdmin(admin.ModelAdmin):
    list_display = ('Duration', 'Price', 'Include')


admin.site.register(Register, RegisterAdmin)
admin.site.register(SignupInfo, SignupInfoAdmin)
admin.site.register(WorkoutExercise, WorkoutExerciseAdmin)
admin.site.register(WorkoutCategory, WorkoutCategoryAdmin)
admin.site.register(WorkoutSubcategory, WorkoutSubcategoryAdmin)
admin.site.register(Packages, PackagesAdmin)

