from django.db import transaction
from apps.shop.models import ShopPost, PurchaseHistory
from apps.clothes.models import FashionItem


class ShopService:
    @staticmethod
    @transaction.atomic
    def create_purchase(shop_post_id, member_id):

        shop_post = ShopPost.objects.select_for_update().select_related(
            'fashion_item'
        ).get(id=shop_post_id)

        if shop_post.status != 'published':
            raise ValueError("구매할 수 없는 상품입니다")

        purchase = PurchaseHistory.objects.create(
            member_id=member_id,
            shop_post=shop_post,
            price=shop_post.price
        )

        shop_post.status = 'completed'
        shop_post.save()

        fashion_item = shop_post.fashion_item
        fashion_item.is_on_sale = False
        fashion_item.save()

        return purchase