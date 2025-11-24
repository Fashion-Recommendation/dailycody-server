from django.db import models


class ShopPostStatus(models.TextChoices):
    PUBLISHED = 'published'
    COMPLETED = 'completed'
    DELETED = 'deleted'


class ShopPost(models.Model):
    member = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE,
        related_name='shop_posts'
    )
    fashion_item = models.ForeignKey(
        'clothes.FashionItem',
        on_delete=models.CASCADE,
        related_name='shop_posts'
    )
    content = models.TextField()
    price = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=ShopPostStatus.choices,
        default=ShopPostStatus.PUBLISHED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shop_post'


class PurchaseHistory(models.Model):
    member = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE,
        related_name='purchase_histories'
    )
    shop_post = models.ForeignKey(
        ShopPost,
        on_delete=models.CASCADE,
        related_name='purchases'
    )
    price=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase_history'
