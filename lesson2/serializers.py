from rest_framework import serializers

from lesson1.models import Student


class StudentSerializer2(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ('name', 'age', 'language')
