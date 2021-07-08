from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    is_send = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
