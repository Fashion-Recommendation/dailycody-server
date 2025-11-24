from rest_framework import serializers

class SnsPostLikeSerializer(serializers.Serializer):
    member_id = serializers.IntegerField(write_only=True)
    liked = serializers.BooleanField(read_only=True)
    like_cnt = serializers.IntegerField(read_only=True)

class SnsFollowSerializer(serializers.Serializer):
    follower_id = serializers.IntegerField(write_only=True)
    followed = serializers.BooleanField(read_only=True)