# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.exceptions import NotFound
from apps.member.models import Member
from apps.member.serializers.info_serializers import MemberInfoSerializer
from apps.member.serializers.info_serializers import MemberInfoUpdateSerializer


class MemberInfo(generics.RetrieveUpdateAPIView):
    queryset = Member.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MemberInfoSerializer   # 조회용
        return MemberInfoUpdateSerializer

    def get_object(self):
        try:
            return Member.objects.get(pk=1)
        except Member.DoesNotExist:
            raise NotFound("Member #1 not found")