from django.urls import path
from .views import ReviewCreateView, BusinessReviewListView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
    path("businesses/<int:id>/reviews/", BusinessReviewListView.as_view(), name="business-reviews"),
    path("reviews/<int:id>/", ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/<int:id>/delete/", ReviewDeleteView.as_view(), name="review-delete"),
]