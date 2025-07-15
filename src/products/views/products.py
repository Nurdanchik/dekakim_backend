from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import status
from products.serializers.product import (
    CategoryWithProductsSerializer,
    ProductSerializer,
    BannerSerializer,
    CategoryWithFlatProductCardsSerializer,
)
from products.services.products import (
    get_all_categories_with_products,
    get_product_by_id,
    get_products_by_category,
    get_banner_by_category_id,
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


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='language',
            description='Filter products by language',
            required=False,
            type=str
        )
    ],
    summary='List categories with flat product cards',
    description='Returns categories with products, where product includes category fields as flat.'
)
class CategoryWithFlatProductCardsView(APIView):
    def get(self, request):
        language = request.query_params.get('language')
        categories = get_all_categories_with_products(language=language)
        serializer = CategoryWithFlatProductCardsSerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='category_id',
            description='ID of the category to get banner for',
            required=True,
            type=int
        )
    ],
    summary='Get banner for category',
    description='Returns banner data for a given category.'
)
class BannerByCategoryView(APIView):
    def get(self, request):
        category_id = request.query_params.get('category_id')
        if not category_id:
            return Response({'detail': 'category_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        banner = get_banner_by_category_id(category_id)
        if not banner:
            return Response({'detail': 'No banner found for this category.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BannerSerializer(banner)
        return Response(serializer.data)