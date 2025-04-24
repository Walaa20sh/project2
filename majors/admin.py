from django.contrib import admin
from .models import Department, Major, Instructor, Course, Student, Enrollment, Grade ,Announcement



admin.site.site_header = "University Admin Panel"
admin.site.site_title = "University Management"
admin.site.index_title = "Welcome to University Admin"


admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Grade)
admin.site.register(Announcement)


