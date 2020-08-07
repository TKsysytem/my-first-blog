""" Djangoの path 関数と、blog アプリの全ての ビューをインポート
"""

from django.urls import path
from . import views

"""
post_list という名前のビューをルートURLに割り当てる
このパターンは誰かがあなたのWebサイトの 'http://127.0.0.1:8000/' というアドレスにアクセスしてきたらviews.post_list
が正しい行き先だということをDjangoに伝える。

name='post_list' は、ビューを識別するために使われるURL の名前

"""

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

