# Generated by Django 5.2 on 2025-04-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAnalysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='time_entered',
            field=models.TimeField(null=True),
        ),
    ]
