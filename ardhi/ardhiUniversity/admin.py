from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('department_name',)
    search_fields=('department_name',)
    list_filter=('department_name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name','code','credits')
    search_fields=('course_name','code','credits')
    list_filter=('course_name','code','credits')

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    list_filter=('name',)

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display=('name','email','type')
    search_fields=('name','email','type')
    list_filter=('name','email','type')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=('name','capacity',)
    search_fields=('name','capacity',)
    list_filter=('name','capacity',)

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display=('year','type','semister','date','start_time','end_time','updated_at')
    search_fields=('year','type','semister','date','start_time','end_time','updated_at')
    list_filter=('year','type','semister','date','start_time','end_time','updated_at')

@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display=('approved_by','approved_by',)
    search_fields=('approved_by','approved_by',)
    list_filter=('approved_by','approved_by',)