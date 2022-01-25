from django.contrib import admin

from .models import Student, Teacher, TeacherStudent


class TeacherStudentInline(admin.TabularInline):
    model = TeacherStudent
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [TeacherStudentInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
