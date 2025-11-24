from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from apps.sns.services.create_services import SnsPostService
from apps.sns.serializers.sns_crud_serializers import (SnsPostUpdateSerializer,
                                                       SnsPostDetailSerializer, SnsPostCreateSerializer)
from apps.sns.models import SnsPost


class SnsPostCreate(generics.CreateAPIView):
    serializer_class = SnsPostCreateSerializer

    def perform_create(self, serializer):
        SnsPostService.create_sns_post(serializer.validated_data)

class SnsPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SnsPost.objects.all()
    lookup_field = 'id'
    def get_serializer_class(self):
        if self.request.method == "GET":
            return SnsPostDetailSerializer
        elif self.request.method == "PATCH":
            return SnsPostUpdateSerializer
        return SnsPostDetailSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"success": True, "deleted": instance.id}, status=status.HTTP_200_OK)