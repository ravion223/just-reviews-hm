from django.urls import path
import reviews.views as views

urlpatterns = [
    path("", views.get_all_reviews, name="reviews"),
]