from rest_framework import serializers


class GenereteImageSerializer(serializers.Serializer):
    image_description = serializers.CharField(min_length=5)
