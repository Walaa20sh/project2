from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# ---------- 1. Departments ----------
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def departments(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                obj = Department.objects.get(pk=pk)
                serializer = DepartmentSerializer(obj)
                return Response(serializer.data)
            except Department.DoesNotExist:
                return Response({'error': 'Not found'}, status=404)
        else:
            data = Department.objects.all()
            serializer = DepartmentSerializer(data, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        obj = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj = Department.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Deleted successfully'})

# ---------- 2. Majors ----------
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def majors(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                obj = Major.objects.get(pk=pk)
                serializer = MajorSerializer(obj)
                return Response(serializer.data)
            except Major.DoesNotExist:
                return Response({'error': 'Not found'}, status=404)
        else:
            data = Major.objects.all()
            serializer = MajorSerializer(data, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MajorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        obj = Major.objects.get(pk=pk)
        serializer = MajorSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj = Major.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Deleted successfully'})

# ---------- 3. Instructors ----------
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def instructors(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                obj = Instructor.objects.get(pk=pk)
                serializer = InstructorSerializer(obj)
                return Response(serializer.data)
            except Instructor.DoesNotExist:
                return Response({'error': 'Not found'}, status=404)
        else:
            data = Instructor.objects.all()
            serializer = InstructorSerializer(data, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        obj = Instructor.objects.get(pk=pk)
        serializer = InstructorSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj = Instructor.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Deleted successfully'})

# ---------- 4. Courses ----------
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def courses(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                obj = Course.objects.get(pk=pk)
                serializer = CourseSerializer(obj)
                return Response(serializer.data)
            except Course.DoesNotExist:
                return Response({'error': 'Not found'}, status=404)
        else:
            data = Course.objects.all()
            serializer = CourseSerializer(data, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        obj = Course.objects.get(pk=pk)
        serializer = CourseSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj = Course.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Deleted successfully'})

# ---------- 5. Students ----------
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def students(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                obj = Student.objects.get(pk=pk)
                serializer = StudentSerializer(obj)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'error': 'Not found'}, status=404)
        else:
            data = Student.objects.all()
            serializer = StudentSerializer(data, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        obj = Student.objects.get(pk=pk)
        serializer = StudentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj = Student.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Deleted successfully'})

# ---------- 6. Enrollments ----------
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def enrollments(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                obj = Enrollment.objects.get(pk=pk)
                serializer = EnrollmentSerializer(obj)
                return Response(serializer.data)
            except Enrollment.DoesNotExist:
                return Response({'error': 'Not found'}, status=404)
        else:
            data = Enrollment.objects.all()
            serializer = EnrollmentSerializer(data, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        obj = Enrollment.objects.get(pk=pk)
        serializer = EnrollmentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj = Enrollment.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Deleted successfully'})

# ---------- 7. Grades ----------
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def grades(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                obj = Grade.objects.get(pk=pk)
                serializer = GradeSerializer(obj)
                return Response(serializer.data)
            except Grade.DoesNotExist:
                return Response({'error': 'Not found'}, status=404)
        else:
            data = Grade.objects.all()
            serializer = GradeSerializer(data, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        obj = Grade.objects.get(pk=pk)
        serializer = GradeSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj = Grade.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Deleted successfully'})

# ---------- 8. Announcements ----------
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def announcements(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                obj = Announcement.objects.get(pk=pk)
                serializer = AnnouncementSerializer(obj)
                return Response(serializer.data)
            except Announcement.DoesNotExist:
                return Response({'error': 'Not found'}, status=404)
        else:
            data = Announcement.objects.all()
            serializer = AnnouncementSerializer(data, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        obj = Announcement.objects.get(pk=pk)
        serializer = AnnouncementSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj = Announcement.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Deleted successfully'})

