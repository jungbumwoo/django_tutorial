from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    print('here, jb {}'.format(my_discount))
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        print('func get_my_discount, obj:{}'.format(obj))
        print('func get_my_discount, self:{}'.format(self))
        return obj.get_discount()
