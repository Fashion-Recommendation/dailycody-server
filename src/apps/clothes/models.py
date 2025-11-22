from django.db import models


class Category(models.TextChoices):
    TOP = 'top'
    BOTTOM = 'bottom'
    OUTER = 'outer'
    SHOES = 'shoes'
    HAT = 'hat'


class Season(models.TextChoices): ## 계절 정보
    SPRING = 'spring'
    SUMMER = 'summer'
    FALL = 'fall'
    WINTER = 'winter'


class FashionItem(models.Model):
    member = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE,
        related_name='fashion_items'
    )
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=Category.choices)
    color = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    season = models.CharField(max_length=20, choices=Season.choices)
    size = models.CharField(max_length=20)
    image_url = models.URLField(max_length=500)
    wear_cnt = models.IntegerField(default=0)
    is_on_sale = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fashion_item'


class FashionHistory(models.Model):
    member = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE,
        related_name='fashion_histories'
    )
    date = models.DateField()
    season = models.CharField(max_length=20, choices=Season.choices)
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'fashion_history'


class FashionHistoryItem(models.Model):
    fashion_history = models.ForeignKey(
        FashionHistory,
        on_delete=models.CASCADE,
        related_name='items'
    )
    fashion_item = models.ForeignKey(
        FashionItem,
        on_delete=models.CASCADE,
        related_name='history_items'
    )

    class Meta:
        db_table = 'fashion_history_item'
