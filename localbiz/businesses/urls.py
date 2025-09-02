from django.urls import path
from .views import (
    BusinessDetailView,
    BusinessListView,
    BusinessCreateView,
    BusinessUPdateView,
    BusinessDeleteView,
    CategoryListCreateView,
)

urlpatterns = [
    path("businesses/", BusinessListView.as_view(), name='business-list'),
    path('businesses/<int:id>/', BusinessDetailView.as_view(), name='business-detail'),
    path('businesses/', BusinessCreateView.as_view(), name='business-create'),
    path('businesses/<int:id>/', BusinessUPdateView.as_view(), name='business-update'),
    path('businesses/<int:id>/', BusinessDeleteView.as_view(), name='business-delete'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]

