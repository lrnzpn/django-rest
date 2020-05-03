# convert data to JSON
from rest_framework import serializers
from .models import Todo

# serializers convert data sent as HTTP requests to Django objects
# and objects to valid response data
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
