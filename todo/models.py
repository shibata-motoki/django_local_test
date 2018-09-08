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

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "task": self.task,
            "dead_time": self.dead_time,
            "created_at": self.created_at,
        }

    class Meta:
        db_table = 'todo'