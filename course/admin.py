from django.contrib import admin

from course.models.course import Course
from course.models.note import Note
from course.models.subject import Subject

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Note)
