from django.conf import settings
from django.db import models
from django.utils import timezone

class Ranking(models.Model):
    ranking_name = models.CharField(max_length=64, null=False)
    ranking_num = models.IntegerField(default=0)
    rank = models.IntegerField()
    app_name = models.CharField(max_length=64)
    download_value = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ranking_name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ranking_name', 'rank'], name='unique_ranking_name_rank')
        ]
# Create your models here.
