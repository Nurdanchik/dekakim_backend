from django.urls import path
from about.views.block import BlockListAPIView

urlpatterns = [
    path('blocks/', BlockListAPIView.as_view(), name='block-list'),
]