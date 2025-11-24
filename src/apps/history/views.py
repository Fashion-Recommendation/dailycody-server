from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.member.models import Member
from apps.clothes.models import FashionHistory, FashionItem, FashionHistoryItem
from .serializers import *


class fashion_history_info(generics.ListAPIView):
    serializer_class = FashionHistoryInfoSerializer

    def get_queryset(self):
        member_id = self.kwargs.get("member_id")
        return FashionHistory.objects.filter(member_id=member_id)

class fashion_history_done(generics.CreateAPIView):
    def get_serializer_class(self):
        return FashionHistoryDoneSerializer