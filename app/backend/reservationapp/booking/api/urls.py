from django.urls import path
from booking.api import views


urlpatterns = [
    path(
        "taken_days_for_calendar/",
        views.TakenDatesViewSet.as_view(),
        name="reservations",
    ),
]
