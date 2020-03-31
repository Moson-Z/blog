#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
from django import template
from ..forms import CommentForm

register = template.Library()

@register.inclusion_tag('comment/inclusions/_form.html', takes_context=True)
def show_comment_form(context, article, form=None):
    if form is None:
        form = CommentForm()
        return {
            'form': form,
            'article': article,
        }

@register.inclusion_tag('comment/inclusions/_list.html', takes_context=True)
def show_comments(context, article):
    comment_list = article.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }