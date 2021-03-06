"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from p_library import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_list),
    path('index/', views.index),
    path("index/book_increment/", views.book_increment),
    path("index/book_decrement/", views.book_decrement),
    path("index/redactions/", views.redaction),
    path('p_lib/', include("p_library.urls"))
    # path("authors", views.AuthorListView.as_view(), name="author_list"),
    # path("author/create", views.AuthorCreateView.as_view(), name="author_create"),
]
