from django.urls import path
from .views import (
    BusinessDetailView,
    BusinessListView,
    BusinessCreateView
)

urlpatterns = [
    path("businesses/", BusinessListView.as_view(), name='business-list'),
    path('businesses/<int:id>/', BusinessDetailView.as_view(), name='business-detail'),
    path('business/', BusinessCreateView.as_view(), name='business-create'),
]
