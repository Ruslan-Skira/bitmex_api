from rest_framework import serializers
from api.models import Order, ORDER_TYPE

# class OrderSerializer(serializers.Serializer):
    # """ 
    # serialize Orders object
    # """

    # orderID=serializers.CharField(read_only=True)
    # symbol=serializers.CharField(required=False, allow_blank=True, max_length=20)
    # volume=serializers.IntegerField(read_only=True),
    # timestamp = serializers.DateTimeField(read_only=True),
    # side=serializers.ChoiceField(choices=ORDER_TYPE, default='sell')
    # price=serializers.FloatField()
    # # account_name=serializers.CharField(required=True, max_length=100)

    # def create(self, validated_data):
    #     """
    #     Create and return a new 'Order' instance, given the validated data.
    #     """
    #     # account_name = validated_data.get('account_name')
    #     # account = Account.objects.findone(name=account_name)
    #     # return Order.object.create(account=account, **validated_data)
    #     return Order.objects.create( account='firs', **validated_data)
        
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing 'Order' instance, given the validated data
    #     """
    #     # TODO: DO I need during update to update id ? i dont think so/
    #     # instance.orderID=validated_data.get('orderID', instance.orderID) 
    #     instance.symbol=validated_data.get('symbol', instance.symbol)
    #     instance.volume = validated_data.get('volume', instance.volume)
    #     instance.timestamp = validated_data.get('timestamp', instance.timestamp)
    #     instance.side = validated_data.get('side', instance.side)
    #     instance.price = validated_data.get('price', instance.price)
    #     return instance
    
    # TODO change to model serializer
    
class OrderSerializer(serializers.ModelSerializer):
    # timestamp = serializers.DateTimeField()
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Order
        fields = [
            'orderID',
            'symbol',
            # 'volume',
            # 'timestamp', 
            'side', 
            # 'price', 
            # 'account'
            ]
