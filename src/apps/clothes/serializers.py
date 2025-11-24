from django.db import transaction
from rest_framework import serializers
from apps.member.models import Member
from apps.clothes.models import FashionItem

class ClosetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionItem
        fields = ["id", "name", "category", "style", "image_url"
                  , "wear_cnt", "is_on_sale", "created_at", "updated_at"]


class ClosetSerializer(serializers.ModelSerializer):
    fashion_items = ClosetItemSerializer(many=True)
    class Meta:
        model = Member
        fields = ["id", "show_closet", "fashion_items"]

class RegisterClothesSerializer(serializers.ModelSerializer):
    member_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = FashionItem
        fields = ["member_id", "name", "content", "size", "color", "style",
                  "category", "season", "image_url"]

    def create(self, validated_data):
        member_id = validated_data.pop('member_id')
        member = Member.objects.get(id=member_id)

        return FashionItem.objects.create(
            member=member,
            **validated_data
        )

class ClothesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionItem
        fields = ["id", "member_id", "name", "content", "category", "style", "season", "size",
                  "image_url","wear_cnt", "is_on_sale", "created_at", "updated_at"]


class ClothesInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionItem
        fields = ["name", "content", "size"]