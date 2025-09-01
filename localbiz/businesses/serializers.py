from rest_framework import serializers
from .models import Business

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__" 
        read_only_fields = ["id", "owner", "created_at"]
        