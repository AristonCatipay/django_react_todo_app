# Convert the model instances to JSON. 
# So that the frontend can work with the recieved data easily.
# JSON is the standard for data interchange.

from rest_framework import serializers
from . models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')