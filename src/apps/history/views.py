from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.member.models import Member
from apps.clothes.models import FashionHistory, FashionItem, FashionHistoryItem
from .serializers import *


class FashionHistoryInfo(generics.ListAPIView):
    serializer_class = FashionHistoryInfoSerializer

    def get_queryset(self):
        member_id = 1
        return FashionHistory.objects.filter(member_id=member_id)


class FashionHistoryDone(generics.CreateAPIView):
    serializer_class = FashionHistoryDoneSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["member_id"] = 1
        return context
