from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .student_serializer import StudentSerializer
from .exceptions import StudentNotFoundException


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Student created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_by_id(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise StudentNotFoundException()

    serializer = StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise StudentNotFoundException()

    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Student updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise StudentNotFoundException()

    student.delete()
    return Response(
        {"message": "Student deleted successfully"},
        status=status.HTTP_200_OK
    )