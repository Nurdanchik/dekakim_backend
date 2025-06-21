from rest_framework import serializers
from about.models.block import Block, BlockPhoto, BlockVideo

class BlockPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockPhoto
        fields = ['id', 'photo']

class BlockVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockVideo
        fields = ['id', 'video']

class BlockSerializer(serializers.ModelSerializer):
    photos = BlockPhotoSerializer(many=True, read_only=True)
    videos = BlockVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Block
        fields = ['id', 'title', 'blocktype', 'language', 'photos', 'videos']