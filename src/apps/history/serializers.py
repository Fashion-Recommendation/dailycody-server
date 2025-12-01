from django.db import transaction
from rest_framework import serializers
from apps.member.models import Member
from apps.clothes.models import FashionItem, FashionHistory, FashionHistoryItem

from apps.history.services import FashionHistoryService


class FashionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionItem
        fields = ["id", "name", "image_url"]

class FashionHistoryItemSerializer(serializers.ModelSerializer):
    fashion_item = FashionItemSerializer()

    class Meta:
        model = FashionHistoryItem
        fields = ["fashion_item"]

class FashionHistoryInfoSerializer(serializers.ModelSerializer):
    items = FashionHistoryItemSerializer(many = True)
    class Meta:
        model = FashionHistory
        fields = [
            "date", "season", "place", "created_at", "items"

        ]


class FashionHistoryDoneSerializer(serializers.ModelSerializer):

    item_ids = serializers.ListField(
        child=serializers.IntegerField(),
    )

    class Meta:
        model = FashionHistory
        fields = ["date", "season", "place", "item_ids"]

    def create(self, data):
        return FashionHistoryService.create_fashion_history(
            member_id=self.context.get("member_id"),
            date=data['date'],
            season=data['season'],
            place=data['place'],
            item_ids=data['item_ids']
        )