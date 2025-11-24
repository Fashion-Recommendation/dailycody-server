from django.db import transaction
from apps.sns.models import SnsPost, SnsPostItem
from apps.member.models import Member


class SnsPostService:

    @staticmethod
    @transaction.atomic
    def create_sns_post(data):

        member = Member.objects.get(id=data["member_id"])

        sns_post = SnsPost.objects.create(
            member=member,
            content=data["content"],
            post_image_url=data["post_image_url"]
        )

        for item_id in data.get("fashion_item_ids", []):
            SnsPostItem.objects.create(
                sns_post=sns_post,
                fashion_item_id=item_id
            )

        return sns_post
