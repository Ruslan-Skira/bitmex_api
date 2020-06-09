from rest_framework import serializers
from api.models import Order, ORDER_TYPE

class OrderSerializer(serializers.Serializer):
    """ 
    serialize Orders object
    """

    orderID=serializers.CharField(read_only=True)
    symbol=serializers.CharField(required=False, allow_blank=True, max_length=20)
    volume=serializers.IntegerField(read_only=True),
    timestamp = serializers.DateTimeField(read_only=True),
    side=serializers.ChoiceField(choices=ORDER_TYPE, default='sell')
    price=serializers.FloatField()
    #TODO clarify how to work with FK fields in Serialization
    # account=serializers.ForeignKey('Account', on_delete=models.CASCADE) 

    def create(self, validated_data):
        """
        Create and return a new 'Order' instance, given the validated data.
        """
        return Order.object.create(**validated_data)
        
    def update(self, instance, validated_data):
        """
        Update and return an existing 'Order' instance, given the validated data
        """
        # TODO: DO I need during update to update id ? i dont think so/
        # instance.orderID=validated_data.get('orderID', instance.orderID) 
        instance.symbol=validated_data.get('symbol', instance.symbol)
        instance.volume = validated_data.get('volume', instance.volume)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.side = validated_data.get('side', instance.side)
        instance.price = validated_data.get('price', instance.price)
        return instance