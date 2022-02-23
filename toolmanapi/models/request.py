from django.db import models


class Request(models.Model):
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='customer_request')
    topic = models.ForeignKey(
        'Topic', on_delete=models.CASCADE, related_name='topic_request')
    description = models.CharField(max_length=500)
    read = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    budget = models.IntegerField()
    status = models.ForeignKey(
        'Status', on_delete=models.CASCADE, related_name='status_request')
