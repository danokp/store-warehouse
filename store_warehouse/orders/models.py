from django.db import models


class SynchConnection(models.Model):
    '''Model for connection to another client using token.'''

    name = models.CharField(max_length=255, unique=True)
    link = models.URLField(max_length=100, unique=True)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    '''Abstract model used for creation StoreOrder and WarehouseOrder models'''

    order_number = models.CharField(max_length=255, unique=True)

    STATUS_CHOICES = (
        ('new', 'New'),
        ('in progress', 'In progress'),
        ('stored', 'Stored'),
        ('send', 'Send'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    prev_status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=None,
        null=True,
    )

    connection = models.ForeignKey(SynchConnection, on_delete=models.PROTECT)

    def __str__(self):
        return f'order: {self.order_number}-{self.connection}-{self.status}'

    class Meta:
        abstract = True
