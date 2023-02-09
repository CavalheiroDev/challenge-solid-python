from utils.repository_interface import Repositories


class IProductsRepository(Repositories):
    def find_by_id(self, product_id):
        raise NotImplementedError()
