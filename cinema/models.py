from django.db import models


class Movie(models.Model):
    title = models.CharField(
        max_length=255,
        null=False
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=255
    )
    duration = models.IntegerField()

    def __str__(self):
        return self.title
