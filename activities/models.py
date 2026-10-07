from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from categories.models import Category, Vibe


class Activity(models.Model):
    class ENVIRONMENT_CHOICES(models.TextChoices):
        OUTDOORS = 'Outdoors'
        INDOORS = 'Indoors'

    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    budget = models.DecimalField(decimal_places=2, max_digits=7, null=False, blank=False
                                 , validators=[MinValueValidator(Decimal('0.00'))])
    environment = models.CharField(choices=ENVIRONMENT_CHOICES, max_length=8)
    distance = models.DecimalField(decimal_places=2, max_digits=8, null=False, blank=False
                                   , validators=[MinValueValidator(Decimal('0.00')),
                                                 MaxValueValidator(Decimal('40075.02'))])
    location = models.CharField(max_length=100, null=False, blank=False)
    dog_friendly = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='activities')
    vibes = models.ManyToManyField(Vibe, related_name='activities')

    def __str__(self):
        return self.name
