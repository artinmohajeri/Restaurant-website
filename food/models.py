from django.db import models

# Create your models here.


class Foods(models.Model):
    types = (
        ('lunch', 'lunch'),
        ('drinks', 'drinks'),
        ('dinner', 'dinner'),
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    type = models.CharField(max_length=6,choices=types,default="lunch")
    picture = models.ImageField(upload_to='food/', default='pic/default_food.png', null=True, blank=True)
    def __str__(self):
        return f"{self.name}  |  {self.description[:200]}"


