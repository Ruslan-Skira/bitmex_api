from django.db import models

BUY = 'buy'
SELL = 'sell'
ORDER_TYPE = [
    (BUY, 'Buy'),
    (SELL, 'Sell'),
]

class Account(models.Model):
    """
    Model for saving connecting parameters to Bitmex wallets
    """
    name = models.CharField(max_length=100, blank=True)
    api_key = models.CharField(max_length=100, blank=True)
    api_secret = models.CharField(max_length=100, blank=True)

class Order(models.Model):
    orderID=models.CharField(max_length=100, blank=True)
    symbol=models.CharField(max_length=20, blank=True, default='USD')
    volume=models.IntegerField(),
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True),
    side=models.CharField(
        max_length=10,
        choices=ORDER_TYPE,
        blank=True,
    )
    price=models.FloatField()
    account=models.ForeignKey('Account', on_delete=models.CASCADE, blank=True)
    
    
    
    # TODO: Clarify how to make ordering by field wich are not exists
    # class Meta:
    #     ordering = [ 'timestamp' ]

