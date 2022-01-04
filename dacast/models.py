from django.db import models


UPLOAD_TYPES = [
    ('ajax', 'ajax'),
    ('curl', 'curl'),
]

class Video(models.Manager):
    source = models.CharField(max_length=250, blank=True, null=True)
    file = models.FileField()
    upload_type = models.CharField(max_length=4, choices=UPLOAD_TYPES, default='ajax')
    dacast_url = models.URLField(blank=True, null=True)
    