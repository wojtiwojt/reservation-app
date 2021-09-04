from django.contrib import admin
from .models import Reservation, Email


class ReservationView(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "email",
        "phone",
        "people_count",
        "check_in",
        "check_out",
    )
    list_filter = ("check_in", "check_out")
    search_fields = (
        "name",
        "surname",
        "email",
        "phone",
        "people_count",
        "check_in",
        "check_out",
    )


admin.site.register(Reservation, ReservationView)
admin.site.register(Email)
admin.site.site_header = "Reservation app - admin panel"
