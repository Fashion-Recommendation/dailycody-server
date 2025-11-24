from rest_framework import serializers
from src.apps.member.models import Member

class MemberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            "id", "username", "email", "gender", "age",
            "height", "weight", "show_closet", "profile_image_url",

        ]

class MemberInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            "gender", "age",
            "height", "weight", "show_closet", "profile_image_url",

        ]
