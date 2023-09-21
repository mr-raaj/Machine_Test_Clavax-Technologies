# admin.py

from django.contrib import admin
from .models import Student

def activate_students(modeladmin, request, queryset):
    queryset.update(is_active=True)

def deactivate_students(modeladmin, request, queryset):
    queryset.update(is_active=False)

activate_students.short_description = "Activate selected students"
deactivate_students.short_description = "Deactivate selected students"

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active')
    actions = [activate_students, deactivate_students]

admin.site.register(Student, StudentAdmin)
