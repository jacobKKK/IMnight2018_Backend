from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework import serializers

from human.models import Profile

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date')


class UserDetailsSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email',
                  'first_name', 'last_name', 'profile')
        read_only_fields = ('email', )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)

        instance.profile.bio = profile_data.get('bio', instance.profile.bio)
        instance.profile.birth_date = profile_data.get(
            'birth_date', instance.profile.birth_date)

        return instance
