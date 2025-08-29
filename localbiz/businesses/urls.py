from django.urls import path
from .views import BusinessListView

urlpatterns = [
    path("businesses/", BusinessListView.as_view(), name='business-list'),
]
