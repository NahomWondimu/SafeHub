from django.db import models

# Create your models here.
class WebPage(models.Model):
    placeHolder = models.CharField(max_length=255)
    time_entered = models.TimeField(null=True)

    '''
    url = models.URLField(max_length=500)  # For the URL being analyzed
    community_score = models.CharField(max_length=255, null=True, blank=True)
    last_analysis_date = models.DateTimeField(null=True, blank=True)
    last_analysis_stats = models.JSONField(null=True, blank=True)  # For the stats dictionary
    redirection_chain = models.JSONField(null=True, blank=True)
    reputation = models.IntegerField(null=True, blank=True)
    times_submitted = models.IntegerField(null=True, blank=True)
    tld = models.CharField(max_length=10, null=True, blank=True)
    virustotal_report = models.URLField(max_length=500, null=True, blank=True)
    time_entered = models.TimeField(auto_now_add=True)
    '''