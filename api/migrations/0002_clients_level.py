# Generated by Django 5.1 on 2024-08-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='level',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
