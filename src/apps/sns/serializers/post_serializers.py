from rest_framework import serializers

from apps.sns.models import SnsPost
from apps.member.models import Member
from apps.clothes.models import FashionItem
from apps.sns.models import SnsPostItem


class MemberSimpleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "username", "profile_image_url"]


class SnsPostItemSerializer(serializers.ModelSerializer):
    member_info = MemberSimpleInfoSerializer(source="member", read_only=True)

    class Meta:
        model = SnsPost
        fields = ["id", "member_info", "content", "post_image_url", "like_cnt", "created_at"]

class FashionItemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionItem
        fields = ["id", "name", "category", "is_on_sale", "image_url"]



class SnsPostFashionItemSerializer(serializers.ModelSerializer):
    fashion_item = FashionItemInfoSerializer(read_only=True)

    class Meta:
        model = SnsPostItem
        fields = ["fashion_item"]







