from django.urls import path
from solid_python.products.views import ProductsCreateAPIView

name = "products"
urlpatterns = [
    path("products/create", ProductsCreateAPIView.as_view()),
]
