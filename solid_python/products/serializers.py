from solid_python.products.models import Products
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        read_only_fields = ["id", "created", "modified"]


class CreateProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    price = serializers.DecimalField(max_digits=17, decimal_places=2)
