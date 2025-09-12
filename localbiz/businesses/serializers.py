from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Business, Category

class BusinessSerializer(serializers.ModelSerializer):
    update_url = serializers.SerializerMethodField(read_only=True) 
    url = serializers.HyperlinkedIdentityField(
        view_name='business-detail',
        lookup_field='pk'
    )
    
    class Meta:
        model = Business
        fields = [
            "url",
            "update_url", 
            "pk", 
            "owner", 
            "category", 
            "name", 
            "description", 
            "location", 
            "address", 
            "website", 
            "created_at",
        ] 
        
        read_only_fields = ["pk", "owner", "created_at"]

    def get_update_url(self, obj):
        request = self.context.get('request') 
        if request is None:
            return None
        return reverse("business-update", kwargs={"pk": obj.pk}, request=request) 


    def validate(self, data):
          if Business.objects.filter(
              name=data['name'],
              location=data['location']
          ).exists():
              raise serializers.ValidationError("This business already exists in this location.")
          return data
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"