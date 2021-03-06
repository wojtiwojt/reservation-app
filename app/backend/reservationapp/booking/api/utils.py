from datetime import date, timedelta
from ..models import Reservation
from django.db.models import Q


# return list of single dates from reservation date range
# objects in list are dictionaries for serializer
def get_single_dates(check_in, check_out):
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    start_date = check_in
    end_date = check_out

    date_list = []
    for single_date in daterange(start_date, end_date):
        date_list.append(
            {
                "date": single_date,
                "day": single_date.day,
                "month": single_date.month,
                "year": single_date.year,
            }
        )
    return date_list


def get_reservations_qs_of_given_dates(check_in, check_out):
    queryset = Reservation.objects.filter(
        Q(check_in__range=(check_in, check_out))
        | Q(check_out__range=(check_in, check_out))
    )
    return queryset
