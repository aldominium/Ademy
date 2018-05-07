from django.contrib import admin

from .models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, ]

admin.site.register(Course, CourseAdmin)
