from django.db import models
from django.utils import timezone

class Testdata(models.Model):
    test_title = models.CharField(max_length=200)
    test_data = models.TextField()
    created_at = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.test_title