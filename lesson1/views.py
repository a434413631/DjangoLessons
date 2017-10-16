from rest_framework import viewsets

from lesson1.models import Student
from lesson1.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('-created')
    serializer_class = StudentSerializer
