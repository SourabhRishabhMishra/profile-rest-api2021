from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ serializers a name field for testing out APIView  """
    name = serializers.CharField(max_length=10)
