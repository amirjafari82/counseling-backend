# Generated by Django 5.0 on 2023-12-24 13:39

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='situation',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Solved', 'Solved')], default='Pending', max_length=30),
        ),
    ]
