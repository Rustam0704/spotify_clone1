# Generated by Django 5.0.3 on 2024-03-15 14:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_remove_album_songs_song_album_alter_artist_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8ffbc8d1-82c5-47d5-9fa1-6a623e6bad79'), primary_key=True, serialize=False),
        ),
    ]
