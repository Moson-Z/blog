import re

import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from .models import Article, Category, Tag


def index(request):
    article_list = Article.objects.all()
    return render(request, 'blog/index.html', context={"article_list": article_list})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])
    article.body = md.convert(article.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    article.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={"article": article})

def archive(request, year, month):
    # article_list = Article.objects.filter(created_time__year=year,
    #                                       created_time__month=month,
    #                                       ).order_by('-created_time')
    article_list = Article.objects.filter().raw("select * from article where year(created_time)=%s and month(created_time)=%s",
                                                params=[year, month])
    print(type(year), type(month))
    print(article_list)
    return render(request, 'blog/index.html', context={'article_list': article_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate)
    return render(request, "blog/index.html", context={"article_list": article_list})

def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    article_list = Article.objects.filter(tag=t)
    return render(request, "blog/index.html", context={"article_list": article_list})
