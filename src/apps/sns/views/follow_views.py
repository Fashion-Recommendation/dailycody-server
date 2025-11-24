from rest_framework import generics, status
from rest_framework.response import Response

from apps.sns.services.follow_services import SnsLikeService
from apps.sns.serializers.follow_serializers import SnsPostLikeSerializer
from apps.sns.serializers.follow_serializers import SnsFollowSerializer

from apps.sns.services.follow_services import SnsFollowService


class SnsPostLike(generics.CreateAPIView):
    serializer_class = SnsPostLikeSerializer

    def post(self, request, post_id):
        member_id = request.data.get("member_id")
        result = SnsLikeService.sns_like(post_id, member_id)

        serializer = SnsPostLikeSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SnsFollow(generics.CreateAPIView):
    serializer_class = SnsFollowSerializer

    def post(self, request, user_id):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        follower_id = serializer.validated_data["follower_id"]
        following_id = user_id

        result = SnsFollowService.toggle_follow(follower_id, following_id)
        return Response(result, status=status.HTTP_200_OK)
