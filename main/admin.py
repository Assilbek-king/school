from django.contrib import admin
from main.models import *
# Register your models here.


class InfoTeacherAdmin(admin.ModelAdmin):
    pass
admin.site.register(InfoTeacher,InfoTeacherAdmin)

class DoljnostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doljnost,DoljnostAdmin)

class SinfAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sinf,SinfAdmin)


class PolAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pol,PolAdmin)

class Student_parentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student_parent,Student_parentAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student,StudentAdmin)

class SubjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subject,SubjectAdmin)

class CorpusAdmin(admin.ModelAdmin):
    pass
admin.site.register(Corpus,CorpusAdmin)

class CabinetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cabinet,CabinetAdmin)

class LessonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lesson,LessonAdmin)

class WeekAdmin(admin.ModelAdmin):
    pass
admin.site.register(Week,WeekAdmin)

class LessonTimeAdmin(admin.ModelAdmin):
    pass
admin.site.register(LessonTime,LessonTimeAdmin)

class DiagnozAdmin(admin.ModelAdmin):
    pass
admin.site.register(Diagnoz,DiagnozAdmin)
