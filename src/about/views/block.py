from rest_framework.generics import ListAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from about.serializers.block import BlockSerializer
from about.services.block import get_blocks_by_type_and_language

class BlockListAPIView(ListAPIView):
    serializer_class = BlockSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='blocktype',
                description='Тип блока: About us, Our vision, Our mission, Res. & Dev.',
                required=True,
                type=str,
                examples=[
                    OpenApiExample(name='About us', value='About us'),
                    OpenApiExample(name='Our mission', value='Our mission')
                ]
            ),
            OpenApiParameter(
                name='language',
                description='Язык: Eng, Tur',
                required=True,
                type=str,
                examples=[
                    OpenApiExample(name='English', value='Eng'),
                    OpenApiExample(name='Turkish', value='Tur')
                ]
            ),
        ]
    )
    def get_queryset(self):
        blocktype = self.request.query_params.get('blocktype')
        language = self.request.query_params.get('language')
        return get_blocks_by_type_and_language(blocktype, language)