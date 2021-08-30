from django.contrib import admin
from .models import Reservation

admin.site.register(Reservation)
admin.site.site_header = "Reservation app - admin panel"
