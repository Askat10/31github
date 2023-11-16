from rest_framework.serializers import ModelSerializer

from applications.account.user_profile.models import ProfileModel


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = [
            'slug', 'user', 'name', 'last_name',
            'birth_date', 'gender', 'bio', 'country'
        ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }
