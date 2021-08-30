from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=256, blank=False)
    surname = models.CharField(max_length=256, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=False)
    people_count = models.IntegerField(blank=False)
    check_in = models.DateField(blank=False)
    check_out = models.DateField(blank=False)

    def __str__(self):
        return f"{self.name} {self.surname} / {self.check_in} - {self.check_out}"

