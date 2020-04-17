#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # path("", views.index, name="index"),
    # path("tag/<int:pk>", views.tag, name="tag"),
    # path("category/<int:pk>", views.category, name="category"),
    # path("archives/<int:year>/<int:month>/", views.archive, name="archive"),
    # path("detail/<int:pk>/", views.detail, name="detail"),
    path("", views.IndexView.as_view(), name="index"),
    path("detail/<int:pk>/", views.AriticleDetailView.as_view(), name="detail"),
    path("archives/<int:year>/<int:month>/", views.ArchiveView.as_view(), name="archive"),
    path("category/<int:pk>", views.CategoryView.as_view(), name="category"),
    path("tag/<int:pk>", views.TagView.as_view(), name="tag"),
    path('search/', views.search, name='search'),
]
