from rest_framework.serializers import ModelSerializer
from applications.course.vocabulary.models import WordsModel


class WordsSerializer(ModelSerializer):
    class Meta:
        model = WordsModel
        fields = [
            'slug', 'eng_word', 'eng_transcription',
            'ru_word', 'part_of_speech', 'level']

        extra_kwargs = {
            'slug': {'read_only': True}
        }
