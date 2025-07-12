from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import status
from products.serializers.product import (
    CategoryWithProductsSerializer,
    ProductSerializer,
    ProductCardsSerializer,
    CategoryWithProductCardsSerializer,
    BannerSerializer,
)
from products.services.products import (
    get_all_categories_with_products,
    get_product_by_id,
    get_products_by_category,
    get_category_with_products_by_language,
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
    


class ProductCardsByCategoryView(APIView):
    def get(self, request, category_id):
        products = get_products_by_category(category_id)
        serializer = ProductCardsSerializer(products, many=True)
        return Response(serializer.data)
    

@extend_schema(
    parameters=[
        OpenApiParameter(
            name='language',
            description='Product language: Eng (English), Tur (Turkish)',
            required=False,
            type=str,
            examples=[
                OpenApiExample(name='English', value='Eng'),
                OpenApiExample(name='Turkish', value='Tur'),
            ]
        ),
    ],
    summary='Detailed cards for one category',
    description='Returns one category with detailed product cards. The category is chosen based on language.'
)
class CategoryCardsByLanguageView(APIView):
    def get(self, request):
        language = request.query_params.get('language', 'Eng')
        category = get_category_with_products_by_language(language)

        if not category:
            return Response({"detail": f"No category found for language '{language}'."}, status=status.HTTP_404_NOT_FOUND)

        # ✅ передаём context с request
        serializer = CategoryWithProductCardsSerializer(category, context={'request': request})
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