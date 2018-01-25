from django.contrib.auth.models import User

from rest_framework import serializers

from human.models import Profile, Relationship,  Reward, Task


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date')


class UserDetailsSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
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

        # update Profile and User sametime
        instance.profile.bio = profile_data.get('bio', instance.profile.bio)
        instance.profile.birth_date = profile_data.get(
            'birth_date', instance.profile.birth_date)

        return instance


class RelationshipSerializer(serializers.ModelSerializer):
    client = UserDetailsSerializer(required=True)
    performer = UserDetailsSerializer(required=True)

    class Meta:
        model = Relationship

        fields = ('client', 'performer', 'created')
        # fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('name', 'description', 'due_date',
                  'credit', 'activated')
        read_only_fields = ('credit')


class RewardSerializer(serializers.ModelSerializer):
    task = TaskSerializer(required=True)
    client = UserDetailsSerializer(required=True)

    class Meta:
        model = Reward
        fields = ('client', 'task', 'rewarded')
