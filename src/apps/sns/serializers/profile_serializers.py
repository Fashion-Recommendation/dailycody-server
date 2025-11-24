from rest_framework import serializers

from apps.sns.models import SnsPost
from apps.member.models import Member
from apps.clothes.models import FashionItem
from apps.sns.models import SnsPostItem


class SnsPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnsPost
        fields = ["id", "post_image_url"]

class SnsClosetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionItem
        fields = ["id", "category", "image_url"]


class SnsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "username", "profile_image_url", "follower_cnt", "following_cnt"
            ,"sns_post_cnt"]


