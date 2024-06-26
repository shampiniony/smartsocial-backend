from apps.core.models import Event, Ticket
from django.core.validators import EmailValidator, MinValueValidator
from django.db import models
from django.db.models import Count, F, Sum


class Buyer(models.Model):
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Cart(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_places(self):
        return self.tickets.aggregate(total_places=Count("id"))["total_places"] or 0

    @property
    def total(self):
        return (
                self.tickets.aggregate(total=Sum(F("ticket__price") * F("quantity")))[
                    "total"
                ]
                or 0
        )


class CartTicket(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="tickets")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    time = models.DateTimeField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    time = models.DateTimeField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    order = models.ForeignKey("payments.Order", on_delete=models.CASCADE, related_name="bookings")
