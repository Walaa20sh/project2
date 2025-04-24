from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.departments),
    path('departments/<int:pk>/', views.departments),

    path('majors/', views.majors),
    path('majors/<int:pk>/', views.majors),

    path('instructors/', views.instructors),
    path('instructors/<int:pk>/', views.instructors),

    path('courses/', views.courses),
    path('courses/<int:pk>/', views.courses),

    path('students/', views.students),
    path('students/<int:pk>/', views.students),

    path('enrollments/', views.enrollments),
    path('enrollments/<int:pk>/', views.enrollments),

    path('grades/', views.grades),
    path('grades/<int:pk>/', views.grades),

    path('announcements/', views.announcements),
    path('announcements/<int:pk>/', views.announcements),
]



