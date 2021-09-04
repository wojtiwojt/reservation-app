from django.db.models.signals import post_save
from django.dispatch import receiver

from booking.models import Reservation, Email

# save uniuque email to databes for mass mail purpose
@receiver(post_save, sender=Reservation)
def add_email_to_db_if_unique(sender, instance, *args, **kwargs):
    if not Email.objects.filter(email=instance.email).exists():
        Email.objects.create(email=instance.email)
