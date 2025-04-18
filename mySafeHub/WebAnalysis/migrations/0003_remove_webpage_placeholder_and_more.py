# Generated by Django 5.2 on 2025-04-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAnalysis', '0002_webpage_time_entered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='placeHolder',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='time_entered',
        ),
        migrations.AddField(
            model_name='webpage',
            name='community_score',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='last_analysis_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='last_analysis_stats',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='redirection_chain',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='reputation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='times_submitted',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='tld',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='webpage',
            name='virustotal_report',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
