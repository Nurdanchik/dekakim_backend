from django.contrib import admin
from about.models.block import Block, BlockPhoto, BlockVideo

class BlockPhotoInline(admin.TabularInline):
    model = BlockPhoto
    extra = 1

class BlockVideoInline(admin.TabularInline):
    model = BlockVideo
    extra = 1

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blocktype', 'language')
    search_fields = ('title', 'blocktype')
    inlines = [BlockPhotoInline, BlockVideoInline]