from django.urls import path
from .views import (
    BusinessDetailView,
    BusinessListView
)

urlpatterns = [
    path("businesses/", BusinessListView.as_view(), name='business-list'),
    path('businesses/<int:id>/', BusinessDetailView.as_view(), name='business-detail'),
]
