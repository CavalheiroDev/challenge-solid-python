from rest_framework.views import APIView
from solid_python.products.serializers import (
    CreateProductSerializer,
    ProductsSerializer,
)
from rest_framework.response import Response
from solid_python.products.models import Products


class ProductsCreateAPIView(APIView):
    def post(self, request):
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        price = float(serializer.validated_data.pop("price"))

        price_to_int = int(f"{price:.2f}".replace(".", ""))

        product = Products.objects.create(
            **serializer.validated_data, price=price_to_int
        )

        ouput = ProductsSerializer(instance=product)

        return Response(data=ouput.data)
