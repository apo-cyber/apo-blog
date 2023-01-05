from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    CATEGORY = (('Mountain', '山のこと'),
                ('Flower', '花のこと'),
                ('Cat', '猫のこと'),
                ('Dailylife', '日常のこと'),)

    title = models.CharField(verbose_name='タイトル', max_length=200)
    content = models.TextField(verbose_name='本文')
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    category = models.CharField(
        verbose_name='カテゴリ', max_length=50, choices=CATEGORY)
    image1 = models.ImageField(verbose_name='イメージ1', upload_to='uploads')
    image2 = models.ImageField(
        verbose_name='イメージ2', upload_to='uploads', blank=True, null=True)
    good = models.IntegerField(default=0)

    def __str__(self):
        return self.title
