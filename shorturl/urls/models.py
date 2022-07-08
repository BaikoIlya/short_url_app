from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Url(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='urls'
    )
    create_date = models.DateTimeField(auto_now_add=True)
    long_url = models.CharField(max_length=200)
    short_url = models.SlugField(unique=True)

    class Meta:
        ordering = ['-create_date']
