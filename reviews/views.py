from django.shortcuts import render
from reviews.models import Review


# Create your views here.


def get_all_reviews(request):
    reviews = Review.objects.all()

    context = {
        "reviews": reviews
    }

    return render(
        request,
        "reviews/index.html",
        context
    )