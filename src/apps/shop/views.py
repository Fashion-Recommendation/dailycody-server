from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from apps.shop.models import ShopPost

from apps.shop.serializers import (ShopPostItemSerializer, ShopPostDetailSerializer,
                                  ShopPostUpdateSerializer, ShopPostOrderSerializer)

# Create your views here.
class ShopPostLists(generics.ListAPIView):
    serializer_class = ShopPostItemSerializer

    def get_queryset(self):
        return ShopPost.objects.order_by("-created_at")

class ShopPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopPost.objects.select_related('fashion_item', 'member')
    lookup_field = "id"

    def get_serializer_class(self):

        if self.request.method == "GET":
            return ShopPostDetailSerializer
        elif self.request.method == "PATCH":
            return ShopPostUpdateSerializer
        return ShopPostDetailSerializer

class ShopPostOrder(generics.CreateAPIView):
    serializer_class = ShopPostOrderSerializer
