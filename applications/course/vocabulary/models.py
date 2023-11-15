from django.db import models
from slugify import slugify


class PartOfSpeech(models.TextChoices):
    no = 'no'
    noun = 'noun'
    pronoun = 'pronoun'
    verb = 'verb'
    adverb = 'adverb'
    adjective = 'adjective'
    preposition = 'preposition'
    conjunction = 'conjunction'
    interjection = 'interjection'


class Level(models.TextChoices):
    no = 'no'
    A1 = 'A1'
    A2 = 'A2'
    B1 = 'B1'
    B2 = 'B2'
    C1 = 'C1'
    C2 = 'C2'


class WordsModel(models.Model):
    slug = models.SlugField(primary_key=True)
    eng_word = models.CharField(max_length=100)
    eng_transcription = models.CharField(max_length=100)
    ru_word = models.CharField(max_length=100)
    part_of_speech = models.CharField(
        max_length=13, choices=PartOfSpeech.choices, default=None
        )
    level = models.CharField(max_length=4, choices=Level.choices, default=None)

    class Meta:
        verbose_name = 'Words'
        verbose_name_plural = 'Words'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.eng_word)
        return super().save(self, *args, **kwargs)

    def __str__(self):
        return self.eng_word
