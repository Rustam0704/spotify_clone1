# Generated by Django 5.0.3 on 2024-03-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_alter_artist_id'),
        ('user', '0004_alter_user_artist_following_alter_user_followings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='artist_following',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='music.artist'),
        ),
    ]
