from django.db import models

# Create your models here.
from django.db import models

class Chat(models.Model):
    room_name = models.CharField(max_length=255)
    message = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.room_name}-{self.message}"
