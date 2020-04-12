from django.db import models


class Recipe(models.Model):
    class DifficultyLevel(models.TextChoices):
        EASY = 'Easy'
        MEDIUM = 'Medium'
        HARD = 'Hard'

    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=400)
    picture = models.FileField()
    difficulty = models.CharField(max_length=10, choices=DifficultyLevel.choices, default=DifficultyLevel.EASY)
    prep_time = models.PositiveIntegerField()
    prep_guide = models.TextField()

    def __str__(self):
        return "Recipe for {}".format(self.name)
