from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight




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
    name = models.CharField(max_length=100, unique=True)
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
    price=models.FloatField() # decimal
    account=models.ForeignKey('Account', on_delete=models.CASCADE, blank=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField(default='sht')
    
    def save(self, *args, **kwargs):
        """
        Use the 'pygments' library to create a hightlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.sybol)
        side = 'side' if self.side else False
        options = {'side': self.side} if self.side else {}
        formatter = HtmlFormatter(style=self.style, side=side, full=True, **options)
        super(Order, self).save(*args, **kwarg)



    #     def save(self, *args, **kwargs):
    # """
    # Use the `pygments` library to create a highlighted HTML
    # representation of the code snippet.
    # """
    # lexer = get_lexer_by_name(self.language)
    # linenos = 'table' if self.linenos else False
    # options = {'title': self.title} if self.title else {}
    # formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                           full=True, **options)
    # self.highlighted = highlight(self.code, lexer, formatter)
    # super(Snippet, self).save(*args, **kwargs)
    
    
    
    
    # TODO: Clarify how to make ordering by field wich are not exists
    # class Meta:
    #     ordering = [ 'timestamp' ]

