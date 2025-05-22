from django.contrib import admin
from .models import Student
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
       list_display = (
        'id',
        'full_name',
        'course',
        'email',
        'contact_number',
        'parent_name',
        'parent_contact_number',
        'is_deleted',  
    )

# Register your models here.

