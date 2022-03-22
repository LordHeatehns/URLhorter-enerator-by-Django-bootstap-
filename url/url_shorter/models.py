from django.db import models
from .utils import create_shorter_url 

# Create your models here.

class Shorter(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveBigIntegerField(default=0)
    long_url = models.URLField(max_length=1500)
    short_url = models.CharField(max_length=15 , unique=True , blank=True)

    class Meta:
        ordering= ["-created"]

    def __str__(self) -> str:
        return f'{self.long_url} to {self.short_url}'

    def save(self , *args ,**kwargs):
        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shorter_url(self)

        super().save(*args , **kwargs)

    
