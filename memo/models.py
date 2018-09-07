from django.db import models
from django.utils import timezone


class Memo(models.Model):

    title = models.CharField('タイトル', max_length=100)
    content = models.TextField('メモ', max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'memo'