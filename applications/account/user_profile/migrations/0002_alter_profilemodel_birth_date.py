# Generated by Django 4.2.7 on 2023-11-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='birth_date',
            field=models.DateField(blank=True, default=None),
        ),
    ]