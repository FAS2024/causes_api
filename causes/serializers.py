from rest_framework import serializers
from .models import Cause, Contribution
from django.contrib.auth.models import User
from rest_framework import serializers


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ['name', 'email', 'amount']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Contribution amount must be greater than zero.")
        return value

class CauseSerializer(serializers.ModelSerializer):
    contributions = ContributionSerializer(many=True, read_only=True)

    class Meta:
        model = Cause
        fields = ['id', 'title', 'description', 'image_url', 'contributions']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
