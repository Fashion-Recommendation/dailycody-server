from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from apps.sns.models import SnsPost
from apps.member.models import Member
from apps.clothes.models import FashionItem
from apps.sns.services.create_services import SnsPostService

from apps.sns.serializers.post_serializers import (SnsPostItemSerializer)
from apps.sns.serializers.profile_serializers import (SnsProfileSerializer, SnsPostListSerializer,
                                                          SnsClosetListSerializer)
from apps.sns.serializers.sns_crud_serializers import (SnsPostCreateSerializer, SnsPostDetailSerializer)


class SnsPostLists(generics.ListAPIView):
    serializer_class = SnsPostItemSerializer

    def get_queryset(self):
        return SnsPost.objects.order_by("-created_at")


