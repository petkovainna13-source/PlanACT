from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Vibe(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

