from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models
from datetime import date

class Task(models.Model):
    
    STATUS = (
        ('doing','Doing'),
        ('done','Done'),
    )

    title = models.CharField(max_length=60,)
    description = models.TextField()
    done = models.CharField(
        max_length=5, 
        choices=STATUS,
        )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    scheduled = models.BooleanField(default=False)
    schedule_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
