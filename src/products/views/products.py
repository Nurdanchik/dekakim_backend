from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from products.serializers.product import (
    CategoryWithProductsSerializer,
    ProductSerializer,
    ProductCardsSerializer,
)
from products.services.products import (
    get_all_categories_with_products,
    get_product_by_id,
    get_products_by_category,
)
from products.models.product import Product


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='language',
            description='Product language: Eng (English), Tur (Turkish)',
            required=False,
            type=str,
            examples=[
                OpenApiExample(
                    name='English example',
                    value='Eng',
                    summary='Example for English'
                ),
                OpenApiExample(
                    name='Turkish example',
                    value='Tur',
                    summary='Example for Turkish'
                ),
            ]
        ),
    ],
    summary='List all categories with their products',
    description='Returns a list of all product categories along with the products inside each category.'
)
class CategoryWithProductsListAPIView(ListAPIView):
    serializer_class = CategoryWithProductsSerializer

    def get_queryset(self):
        language = self.request.query_params.get('language')
        return get_all_categories_with_products(language)


@extend_schema(
    summary='Retrieve product details by ID',
    description='Returns detailed information about a product by its ID.'
)
class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_object(self):
        return get_product_by_id(self.kwargs['pk'])
    


class ProductCardsByCategoryView(APIView):
    def get(self, request, category_id):
        products = get_products_by_category(category_id)
        serializer = ProductCardsSerializer(products, many=True)
        return Response(serializer.data)