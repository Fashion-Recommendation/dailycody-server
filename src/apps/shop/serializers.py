from django.db import transaction
from rest_framework import serializers
from apps.shop.models import ShopPost
from apps.clothes.models import FashionItem
from apps.member.models import Member
from apps.shop.models import PurchaseHistory
from apps.shop.services import ShopService


class FashionItemSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionItem
        fields = ["id", "category", "name", "color", "image_url", "style", "season", "size"]

class SellerSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "username", "profile_image_url"]

class ShopPostItemSerializer(serializers.ModelSerializer):
    fashion_item = FashionItemSimpleSerializer(read_only=True)

    class Meta:
        model = ShopPost
        fields = ["id", "price", "status", "fashion_item","created_at"]



class ShopPostDetailSerializer(serializers.ModelSerializer):
    fashion_item = FashionItemSimpleSerializer(read_only=True)
    seller_info = SellerSimpleSerializer(source='member', read_only=True)

    class Meta:
        model = ShopPost
        fields = ["id", "seller_info", "content", "price", "status", "fashion_item","created_at"]

class ShopPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopPost
        fields = ["content", "price"]


class ShopPostOrderSerializer(serializers.ModelSerializer):
    shop_post_id = serializers.IntegerField(write_only=True)
    member_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PurchaseHistory
        fields = ["shop_post_id", "member_id"]

    def create(self, validated_data):
        return ShopService.create_purchase(
            shop_post_id=validated_data['shop_post_id'],
            member_id=validated_data['member_id']
        )