from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    business = serializers.StringRelatedField(read_only=True)
    stars = serializers.ReadOnlyField()
    
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ['id', 'user', 'business', 'stars', 'created_at', 'updated_at']