from django.db import models
from django.core.validators import MinValueValidator

COLOR_CHOICES = (
    ("-", "-"),
    ("BLACK", "Black"),
    ("WHITE", "White"),
    ("GRAY", "Gray"),
    ("BLUE", "Blue"),
    ("RED", "Red"),
    ("BROWN", "Brown"),
    ("BEIGE", "Beige"),
    ("ORANGE", "Orange"),
    ("YELLOW", "Yellow"),
    ("GOLD", "Gold"),
)


class CarModel(models.Model):
    name = models.CharField(max_length=28)
    length = models.BigIntegerField(validators=[MinValueValidator(1300)])  # mm
    width = models.BigIntegerField(validators=[MinValueValidator(1000)])  # mm
    weight = models.BigIntegerField(validators=[MinValueValidator(450)])  # kg
    velocity = models.DecimalField(decimal_places=2, max_digits=8)  # m/s
    color = models.CharField(max_length=16, choices=COLOR_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cars"
