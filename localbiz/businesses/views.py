from django.shortcuts import render
from rest_framework import generics, filters, permissions
from .models import Business, Category
from .serializers import BusinessSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly 

# list all businesses 
class BusinessListView(generics.ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer 
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ['name', 'description', 'location']
    filterset_fields = ['category', 'owner', 'location']
    ordering_fields = ['name', 'created_at'] 

# Retrieve business by id
class BusinessDetailView(generics.RetrieveAPIView): 
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    lookup_field = "id"
    permission_classes = [permissions.IsAuthenticated]

# Create business instance 
class BusinessCreateView(generics.CreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

# Update business
class BusinessUPdateView(generics.UpdateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
 

# Delete business
class BusinessDeleteView(generics.DestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

 
# List all business categories
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()] 
