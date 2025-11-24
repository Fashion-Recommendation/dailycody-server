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


class SnsProfile(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    lookup_field = 'id'
    serializer_class = SnsProfileSerializer

class SnsProfilePosts(generics.ListAPIView):
    serializer_class = SnsPostListSerializer

    def get_queryset(self):
        member_id = self.kwargs.get('id')
        return SnsPost.objects.filter(
            member_id=member_id
        ).order_by('-created_at')

class SnsClosetLists(generics.ListAPIView):
    serializer_class = SnsClosetListSerializer

    def get_queryset(self):
        member_id = self.kwargs.get('id')
        return FashionItem.objects.filter(
            member_id=member_id
        ).order_by('-created_at')