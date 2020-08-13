from django.db import models

class Word (models.Model):
    title = models.CharField(max_length = 120)
    define = models.TextField()
    example = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title