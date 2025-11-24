from django.db import transaction
from apps.member.models import Member
from apps.clothes.models import FashionItem, FashionHistory, FashionHistoryItem

class FashionHistoryService:

    @staticmethod
    @transaction.atomic
    def create_fashion_history(member_id, date, season, place, item_ids):

        member = Member.objects.get(id=member_id)

        fashion_history = FashionHistory.objects.create(
            member=member,
            date=date,
            season=season,
            place=place
        )

        history_items = [
            FashionHistoryItem(
                fashion_history=fashion_history,
                fashion_item_id=item_id
            )
            for item_id in item_ids
        ]

        FashionHistoryItem.objects.bulk_create(history_items)

        return fashion_history