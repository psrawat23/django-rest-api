from rest_framework import serializers


# serializers are used to converts objects in to data type used by front end
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

