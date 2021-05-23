from rest_framework import serializers
from generationapp.models import IdStamp

class IdStampSerializer(serializers.ModelSerializer):
    """
    serializer for IdStamp
    """
    class Meta:
        model = IdStamp
        fields = ['id', 'timestamp']
