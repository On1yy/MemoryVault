from django.utils import timezone
from django.db import models


from django.contrib.auth.models import User


class Memory(models.Model):
    user = models.ForeignKey(
        User,on_delete=models.CASCADE

    )
    title = models.CharField(max_length=60)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
