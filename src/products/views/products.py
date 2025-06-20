from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.serializers import (
    CategoryWithProductsSerializer,
    ProductSerializer,
)
from products.services.products import (
    get_all_categories_with_products,
    get_product_by_id,
)
from products.models import Product


class CategoryWithProductsListAPIView(ListAPIView):
    """
    Возвращает список всех категорий с продуктами внутри
    """
    serializer_class = CategoryWithProductsSerializer

    def get_queryset(self):
        return get_all_categories_with_products()


class ProductDetailAPIView(RetrieveAPIView):
    """
    Подробная информация о продукте по ID
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()  # fallback if service не используется

    def get_object(self):
        return get_product_by_id(self.kwargs['pk'])