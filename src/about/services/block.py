from about.models.block import Block

def get_blocks_by_type_and_language(blocktype, language):
    return Block.objects.filter(blocktype=blocktype, language=language)