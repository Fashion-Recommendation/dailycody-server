from rest_framework import serializers

from apps.sns.models import SnsPost
from apps.member.models import Member
from apps.clothes.models import FashionItem
from apps.sns.models import SnsPostItem
from apps.sns.serializers.post_serializers import MemberSimpleInfoSerializer, SnsPostFashionItemSerializer


class SnsPostCreateSerializer(serializers.ModelSerializer):
    member_id = serializers.IntegerField(write_only=True)
    fashion_item_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only = True
    )
    class Meta:
        model = SnsPost
        fields = ["member_id","content", "post_image_url", "fashion_item_ids"]

class SnsPostDetailSerializer(serializers.ModelSerializer):

    member_info = MemberSimpleInfoSerializer(source="member", read_only=True)
    fashion_items = SnsPostFashionItemSerializer(
        source="items",
        many=True,
        read_only=True
    )

    class Meta:
        model = SnsPost
        fields = ["id","content", "post_image_url", "like_cnt",
                  "created_at", "member_info", "fashion_items"]

class SnsPostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SnsPost
        fields = ["content", "post_image_url"]

class SnsPostDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnsPost
        fields = ["is_deleted"]



