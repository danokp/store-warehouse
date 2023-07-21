from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=255)

    STATUS_CHOICES = (
        ('new', 'New'),
        ('in progress', 'In progress'),
        ('stored', 'Stored'),
        ('send', 'Send'),
    )
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)


    def __str__(self):
        return f'{self.order_number}-{self.status}'

    class Meta:
        abstract = True