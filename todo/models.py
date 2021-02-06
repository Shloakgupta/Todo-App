from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=200)
    complete_or_not = models.BooleanField()

    def __str__(self):
        return self.text
