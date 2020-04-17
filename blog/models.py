#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
import markdown
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags


class Category(models.Model):

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        db_table = 'category'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)


class Tag(models.Model):

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        db_table = 'tag'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)


class Article(models.Model):

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        db_table = 'article'
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    title = models.CharField("标题", max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField("正文")
    category = models.ForeignKey(Category, verbose_name="类别", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name="标签", blank=True)
    created_time = models.DateTimeField("创建时间", default=timezone.now)
    modified_time = models.DateTimeField("修改时间")
    excerpt = models.CharField("摘要", max_length=200, blank=True)
    views = models.PositiveIntegerField(default=0, editable=False)
