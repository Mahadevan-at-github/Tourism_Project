from .models import *
from rest_framework import serializers


class TourismSerializer(serializers.ModelSerializer):
    Destination_Img = serializers.ImageField(required=False)

    class Meta:

        model = Tourism
        fields = ('__all__')
