from django.db import models
from django.utils import timezone


class Todo(models.Model):

    title = models.CharField('タイトル', max_length=100)
    task = models.TextField('やること', max_length=300)
    dead_time = models.DateTimeField('期限',
               default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo'