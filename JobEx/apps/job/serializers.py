from .models import Job
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    posted_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    payment_period = serializers.StringRelatedField()

    class Meta:
        model = Job
        fields = '__all__'  