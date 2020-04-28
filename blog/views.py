import re

import markdown
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from markdown.extensions.toc import TocExtension
from pure_pagination import PaginationMixin

from .models import Article, Category, Tag


class IndexView(PaginationMixin, ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 6


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        print(cate)
        print(type(cate))
        a = Article.objects.filter(category=cate).count()
        print(a)
        return super(CategoryView, self).get_queryset().filter(category=cate)

class TagView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tag=cate)

class AriticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        response = super(DetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

class ArchiveView(IndexView):
    def get_queryset(self):
        # article_list = Article.objects.filter().raw("select * from article where year(created_time)=%s and month(created_time)=%s",
        #                                             params=[self.kwargs.get('year'), self.kwargs.get('month')])
        return super(ArchiveView, self).get_queryset().filter().raw("select * from article where year(created_time)=%s and month(created_time)=%s",
                                                    params=[self.kwargs.get('year'), self.kwargs.get('month')])


def search(request):
    q = request.GET.get('q')

    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    article_list = Article.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'article_list': article_list})

# def detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#
#     article.increase_views()
#     md = markdown.Markdown(extensions=[
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#         # 'markdown.extensions.toc',
#         TocExtension(slugify=slugify),
#     ])
#     article.body = md.convert(article.body)
#
#     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
#     article.toc = m.group(1) if m is not None else ''
#
#     return render(request, 'blog/detail.html', context={"article": article})

# def index(request):
#     article_list = Article.objects.all()
#     paginator = Paginator(article_list, 6)
#     page = request.GET.get('page')
#     try:
#         article_list = paginator.page(page)
#     except PageNotAnInteger:
#         article_list = paginator.page(1)
#     except EmptyPage:
#         article_list = paginator.page(paginator.num_pages)
#     return render(request, 'blog/index.html', context={"article_list": article_list, "paginator": paginator})

# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     article_list = Article.objects.filter(category=cate)
#     return render(request, "blog/index.html", context={"article_list": article_list})

# def tag(request, pk):
#     t = get_object_or_404(Tag, pk=pk)
#     article_list = Article.objects.filter(tag=t)
#     return render(request, "blog/index.html", context={"article_list": article_list})

# def archive(request, year, month):
#     # article_list = Article.objects.filter(created_time__year=year,
#     #                                       created_time__month=month,
#     #                                       ).order_by('-created_time')
#     article_list = Article.objects.filter().raw("select * from article where year(created_time)=%s and month(created_time)=%s",
#                                                 params=[year, month])
#     # print(type(year), type(month))
#     # print(article_list)
#     return render(request, 'blog/index.html', context={'article_list': article_list})



