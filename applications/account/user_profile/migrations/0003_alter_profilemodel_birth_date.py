# Generated by Django 4.2.7 on 2023-11-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_profilemodel_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='birth_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
