from rest_framework.generics import ListAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from about.serializers.block import BlockSerializer
from about.services.block import get_blocks_by_type_and_language


@extend_schema(
    summary='List blocks by type and language',
    description='Returns blocks filtered by their type and language.',
    parameters=[
        OpenApiParameter(
            name='blocktype',
            description='Block type: About us, Our vision, Our mission, Res. & Dev.',
            required=True,
            type=str,
            examples=[
                OpenApiExample(name='About us', value='About us'),
                OpenApiExample(name='Our mission', value='Our mission'),
                OpenApiExample(name='Our vision', value='Our vision'),
                OpenApiExample(name='Res. & Dev.', value='Res. & Dev.')
            ]
        ),
        OpenApiParameter(
            name='language',
            description='Language: Eng (English), Tur (Turkish)',
            required=True,
            type=str,
            examples=[
                OpenApiExample(name='English', value='Eng'),
                OpenApiExample(name='Turkish', value='Tur')
            ]
        ),
    ]
)
class BlockListAPIView(ListAPIView):
    serializer_class = BlockSerializer

    def get_queryset(self):
        blocktype = self.request.query_params.get('blocktype')
        language = self.request.query_params.get('language')
        return get_blocks_by_type_and_language(blocktype, language)