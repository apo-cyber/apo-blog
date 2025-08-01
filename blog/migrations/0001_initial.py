# Generated by Django 4.1.5 on 2023-01-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='本文')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('category', models.CharField(choices=[('Mountain', '山のこと'), ('Flower', '花のこと'), ('Cat', '猫のこと'), ('Dailylife', '日常のこと')], max_length=50, verbose_name='カテゴリ')),
                ('image1', models.ImageField(upload_to='uploads', verbose_name='イメージ1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='イメージ2')),
                ('good', models.IntegerField(default=0)),
            ],
        ),
    ]
