from django.db import models


class RequestPhoto(models.Model):
    image_url = models.URLField(max_length=1000, blank=True)
    request = models.ForeignKey(
        'Request', on_delete=models.CASCADE, related_name='request_photo')
