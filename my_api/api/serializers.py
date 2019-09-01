from rest_framework import serializers
from my_api.models import Students

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'name', 'roll', 'reg', 'marks')