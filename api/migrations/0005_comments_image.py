# Generated by Django 5.1 on 2024-08-18 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_comments_status_faqs_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
