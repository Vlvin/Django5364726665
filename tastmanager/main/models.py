from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('название', max_length=50)
    task = models.TextField('контент')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"