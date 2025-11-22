from django.db import models


class SnsPost(models.Model):
    member = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE,
        related_name='sns_posts'
    )
    content = models.TextField()
    like_cnt = models.IntegerField(default=0)
    post_image_url = models.URLField(max_length=500)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sns_post'


class SnsPostItem(models.Model):
    sns_post = models.ForeignKey(
        SnsPost,
        on_delete=models.CASCADE,
        related_name='items'
    )
    fashion_item = models.ForeignKey(
        'clothes.FashionItem',
        on_delete=models.CASCADE,
        related_name='sns_post_items'
    )

    class Meta:
        db_table = 'sns_post_item'


class SnsFollow(models.Model):
    following = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE,
        related_name='followers'
    )
    follower = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE,
        related_name='following'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sns_follow'
        unique_together = ['following', 'follower']


class SnsLike(models.Model):
    member = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE,
        related_name='sns_likes'
    )
    sns_post = models.ForeignKey(
        SnsPost,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sns_like'
        unique_together = ['member', 'sns_post']
