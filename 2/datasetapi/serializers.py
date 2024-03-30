from rest_framework import serializers
from . import models

class StockSerializer(serializers.ModelSerializer):
    """
    Stock model serializer class
    """
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=5, coerce_to_string=False)
    quantity = serializers.IntegerField()
    status = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    last_updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    def validate_name(self, value):
        """
        validate duplicate names in products
        """
        if models.Stock.objects.filter(name=value).exists():
            raise serializers.ValidationError("Product already exist")
        return value

    def get_status(self, obj):
        """
        Get the status of the product in stock
        """
        if obj.quantity <= 0:
            return "out of stock"
        return "in stock"

    class Meta:
        model = models.Stock
        fields = "__all__"
