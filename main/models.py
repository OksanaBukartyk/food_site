from django.db import models

# Create your models here.

class Dish(models.Model):
    title = models.CharField(max_length=30)
    image =  models.ImageField(upload_to='images/')
    description = models.TextField(max_length=1500)
    time = models.IntegerField(default=0)
    complexity_choices = (
        ('Легко', 'Легко'),
        ('Нормально', 'Нормально'),
        ('Складно', 'Складно'),
    )
    complexity = models.CharField(max_length = 50, choices=complexity_choices)
    portions =  models.IntegerField(default=0)
    video_url = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} {self.description[:20]}..."


class Ingredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="ingredients")
    title  = models.CharField(max_length=30)
    count = models.IntegerField(default=0)
    variable_choices = (
        ('кг', 'кг'),
        ('г', 'г'),
        ('л', 'л'),
        ('мл', 'мл'),
        ('шт', 'шт'),
        ('ч.л', 'ч.л'),
        ('ст.л', 'ст.л'),
    )
    variable = models.CharField(max_length = 50,  choices=variable_choices)


    def __str__(self):
        return f"{self.title}"
