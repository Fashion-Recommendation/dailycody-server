from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from apps.clothes.serializers import ClosetSerializer

from apps.member.models import Member
from apps.clothes.models import FashionItem

from apps.clothes.serializers import RegisterClothesSerializer

from apps.clothes.serializers import ClothesInfoUpdateSerializer, ClothesInfoSerializer


class ClosetInfo(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = ClosetSerializer
    lookup_field = "id"

class RegisterClothes(generics.CreateAPIView):
    serializer_class = RegisterClothesSerializer


class DetailClothes(generics.RetrieveUpdateAPIView):
    queryset = FashionItem.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ClothesInfoSerializer
        else:# 조회용
            return ClothesInfoUpdateSerializer