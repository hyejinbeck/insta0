# Generated by Django 4.2.4 on 2023-08-31 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_post_like_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="like_user",
            new_name="like_users",
        ),
    ]
