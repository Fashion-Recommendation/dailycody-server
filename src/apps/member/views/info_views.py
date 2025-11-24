# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView

from src.apps.member.models import Member
from src.apps.member.serializers.info_serializers import MemberInfoSerializer
from src.apps.member.serializers.info_serializers import MemberInfoUpdateSerializer


class member_info(generics.RetrieveUpdateAPIView):
    queryset = Member.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MemberInfoSerializer   # 조회용
        return MemberInfoUpdateSerializer