from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=3, primary_key=True, validators=[MinLengthValidator(3)])
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Item(models.Model):
    name = models.CharField(max_length=50, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.cat.code})'
    