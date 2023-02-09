from solid_python.products.contracts import IProductsRepository
from solid_python.products.models import Products


class ProductsRepository(IProductsRepository):
    model = Products

    def find_by_id(self, product_id):
        return self.safe_get(id=product_id)
