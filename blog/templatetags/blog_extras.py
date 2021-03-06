#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
from django import template
from django.db.models import Count

from blog.models import Article, Category, Tag

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_article(context, num=5):
    return {
        'recent_article_list': Article.objects.all().order_by('-created_time')[:num],
    }

@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Article.objects.dates('created_time', 'month', order='DESC'),
    }

@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)
    return {
        # 'category_list': Category.objects.all(),
        'category_list': category_list,
    }

@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_this_category(context, article):
    # category_list = Category.objects.annotate(num_articles=Count('article')).filter(name=article.category)
    category_list = Category.objects.filter(name=article.category.name)
    return {
        # 'category_list': Category.objects.all(),
        'category_list': category_list,
    }

@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    tag_list = Tag.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)
    return {
        # 'tag_list': Tag.objects.all(),
        'tag_list': tag_list,
    }

@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_this_tag(context, article):
    tag_list = Tag.objects.filter(name__in=[t.name for t in article.tag.all()])
    return {
        'tag_list': tag_list,
    }