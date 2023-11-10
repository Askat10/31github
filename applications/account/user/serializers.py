from rest_framework import serializers, status
from django.contrib.auth import get_user_model, password_validation
from applications.account import utils

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(
        max_length=200, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation')
        extra_kwargs = {
            'password': {'write_only': True},

        }

    def validate_password(self, password):
        password_validation.validate_password(
            password, self.Meta.model)
        return password

    def validate(self, attrs: dict):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                {'message': 'passwords must match'},
                code=status.HTTP_400_BAD_REQUEST)
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        utils.create_activation_code(user)
        utils.send_activation_code(user)
        return user
