# Generated by Django 5.0 on 2024-04-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_alter_comment_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='answered',
            field=models.BooleanField(default=False),
        ),
    ]
