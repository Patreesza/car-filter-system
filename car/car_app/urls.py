from django.urls import path
from car_app.views import CarListView

urlpatterns = [
    path("", CarListView.as_view(), name="car-list"),
]
