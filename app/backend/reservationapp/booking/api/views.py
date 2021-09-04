from rest_framework import generics
from .serializers import DatesForCalendarSerializer
from booking.models import Reservation
from .utils import get_single_dates, get_reservations_qs_of_given_dates


# returns list of single days of all reservations in given date range
class TakenDatesViewSet(generics.ListAPIView):
    serializer_class = DatesForCalendarSerializer

    def get_queryset(self):
        check_in = self.request.query_params.get("check_in", None)
        check_out = self.request.query_params.get("check_out", None)
        if check_in is not None and check_out is not None:
            given_date_reservation_qs = get_reservations_qs_of_given_dates(
                check_in=check_in, check_out=check_out
            )
            single_dates_of_reservations_list = []
            for reservation in given_date_reservation_qs:
                single_dates_of_reservations_list.append(
                    get_single_dates(reservation.check_in, reservation.check_out)
                )

            single_dates_flat_list = []
            for single_list_of_reservation in single_dates_of_reservations_list:
                for single_date in single_list_of_reservation:
                    single_dates_flat_list.append(single_date)
            return single_dates_flat_list
        return None
