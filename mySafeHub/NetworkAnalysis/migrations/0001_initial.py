# Generated by Django 5.2 on 2025-04-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeHolder', models.CharField(max_length=255)),
                ('time_entered', models.TimeField(null=True)),
            ],
        ),
    ]
