from django.db import models

# Create your models here.
class WebPage(models.Model):
    # For the URL being analyzed
    url = models.URLField(max_length=500, null=True)
    community_score = models.CharField(max_length=255, null=True, blank=True)
    last_analysis_date = models.DateTimeField(null=True, blank=True)
    # For the stats dictionary
    last_analysis_stats = models.JSONField(null=True, blank=True)
    redirection_chain = models.JSONField(null=True, blank=True)
    reputation = models.IntegerField(null=True, blank=True)
    times_submitted = models.IntegerField(null=True, blank=True)
    tld = models.CharField(max_length=10, null=True, blank=True)
    virustotal_report = models.URLField(max_length=500, null=True, blank=True)
    time_entered = models.TimeField(auto_now_add=True, null=True)