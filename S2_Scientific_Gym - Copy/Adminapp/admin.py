from django.contrib import admin
from Adminapp.models import Register, SignupInfo, SubExercise, CatExercise, WorkoutCategory, WorkoutSubcategory, Packages, Exec_Sub_Info, Trainer

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Location', 'Message')


class SignupInfoAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Email', 'Password', 'Mobile')


class SubExerciseAdmin(admin.ModelAdmin):
    list_display = ('Exer_Name', 'Image', 'Description', 'Subcategory')


class CatExerciseAdmin(admin.ModelAdmin):
    list_display = ('Exer_Name', 'Image', 'Description', 'Category')


class WorkoutSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('Sub_Name', 'Image', 'Description', 'Category')


class WorkoutCategoryAdmin(admin.ModelAdmin):
    list_display = ( 'Cat_Name', 'Cat_Image', 'Cat_Logo','Cat_Description')


class PackagesAdmin(admin.ModelAdmin):
    list_display = ('Duration', 'Price', 'Include')


class Exec_Sub_InfoAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'Subcategory')


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('Name','Image','Work','Weight','Height','Email','Contact','Address','Specialities','Qualification','Achievement','Description')


admin.site.register(Register, RegisterAdmin)
admin.site.register(SignupInfo, SignupInfoAdmin)
admin.site.register(SubExercise, SubExerciseAdmin)
admin.site.register(WorkoutCategory, WorkoutCategoryAdmin)
admin.site.register(WorkoutSubcategory, WorkoutSubcategoryAdmin)
admin.site.register(Packages, PackagesAdmin)
admin.site.register(Exec_Sub_Info, Exec_Sub_InfoAdmin)
admin.site.register(CatExercise, CatExerciseAdmin)
admin.site.register(Trainer,  TrainerAdmin)

