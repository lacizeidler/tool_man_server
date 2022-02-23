from django.db import models 

class Message(models.Model):
    sender = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='message_sender')
    message = models.CharField(max_length=500)
    read = models.BooleanField()
    request = models.ForeignKey('Request', on_delete=models.CASCADE, related_name='message_request')
    timestamp = models.DateTimeField(auto_now_add=True)