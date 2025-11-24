from django.db import transaction

from apps.sns.models import SnsLike
from apps.member.models import Member
from apps.sns.models import SnsPost, SnsFollow


class SnsLikeService:

    @staticmethod
    @transaction.atomic
    def sns_like(post_id, member_id):
        post = SnsPost.objects.get(id=post_id)
        member = Member.objects.get(id=member_id)

        like = SnsLike.objects.filter(sns_post=post, member=member)

        if like.exists():
            like.delete()
            post.like_cnt -= 1
            post.save()
            return {"liked": False, "like_cnt": post.like_cnt}

        SnsLike.objects.create(sns_post=post, member=member)
        post.like_cnt += 1
        post.save()
        return {"liked": True, "like_cnt": post.like_cnt}

class SnsFollowService:
    @staticmethod
    @transaction.atomic
    def toggle_follow(follower_id, following_id):
        follower = Member.objects.get(id=follower_id)
        following = Member.objects.get(id=following_id)

        relation = SnsFollow.objects.filter(follower=follower, following=following)

        if relation.exists():
            relation.delete()
            follower.following_cnt -= 1
            follower.save()
            following.follower_cnt -= 1
            following.save()
            return {"followed": False}

        SnsFollow.objects.create(follower=follower, following=following)

        follower.following_cnt += 1
        following.follower_cnt += 1

        follower.save()
        following.save()

        return {"followed": True}
