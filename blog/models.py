from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
import os


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

    def _convert_to_jpg(self, image_field):
        if not image_field:
            return
        ext = os.path.splitext(image_field.name)[1].lower()
        if ext in ['.heic', '.heif']:
            img = Image.open(image_field)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            output = BytesIO()
            img.save(output, format='JPEG', quality=85)
            output.seek(0)
            new_name = os.path.splitext(image_field.name)[0] + '.jpg'
            image_field.save(new_name, ContentFile(output.read()), save=False)

    def save(self, *args, **kwargs):
        self._convert_to_jpg(self.image1)
        self._convert_to_jpg(self.image2)
        super().save(*args, **kwargs)
