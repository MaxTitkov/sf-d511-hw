from django.urls import path
from p_library import views

app_name = "p_library"

urlpatterns = [
    path("authors", views.AuthorListView.as_view(), name="author_list"),
    path("author/create", views.AuthorCreateView.as_view(), name="author_create"),
    path("authors/create_many", views.author_create_many, name='author_create_many'),
    path("authors/create_many_books", views.books_authors_create_many, name="book_author_create_many"),
    path("books_list", views.BooksListView.as_view(), name="books_list"),
    path("book_update<int:pk>", views.BookUpdateView.as_view(), name="book_update_view"),
]