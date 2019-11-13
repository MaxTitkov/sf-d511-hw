from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from p_library.models import Book, Redaction
from django.template import loader
from p_library.models import Author
from p_library.forms import AuthorForm, BookForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template("index.html")
    books = Book.objects.all()
    biblio_data = {"title": "мою библиотеку", 'books': books}
    return HttpResponse(template.render(biblio_data, request))

@csrf_exempt
def book_increment(request):
    if request.method == "POST":
        book_id = request.POST["id"]
        if not book_id:
            return redirect("/index/")
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect("/index/")
            book.copy_count += 1
            book.save()
        return redirect("/index/")
    else:
        return redirect("index/")

@csrf_exempt
def book_decrement(request):
    if request.method == "POST":
        book_id = request.POST["id"]
        if not book_id:
            return redirect("/index/")
        else:
            book = Book.objects.filter(id = book_id).first()
            if not book:
                return redirect("/index/")
            if book.copy_count < 0:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect("/index/")
    else:
        return redirect("/index/")

def redaction(request):
    template = loader.get_template("redactions.html")
    books = Book.objects.all()
    redactions = Redaction.objects.all()
    books_data = {"books": books, "redactions": redactions}
    return HttpResponse(template.render(books_data))


class AuthorListView(ListView):
    model = Author
    template_name = 'authors_list.html'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("p_library:author_list")
    template_name = "authors_edit.html"

def author_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  #  Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  #  Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  #  Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if author_formset.is_valid():  #  Проверяем, валидны ли данные формы
            for author_form in author_formset:  
                author_form.save()  #  Сохраним каждую форму в формсете
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  #  После чего, переадресуем браузер на список всех авторов.
    else:  #  Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(prefix='authors')  #  Инициализируем формсет и ниже передаём его в контекст шаблона.
    return render(request, 'manage_authors.html', {'author_formset': author_formset})

def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BooksFormSet = formset_factory(BookForm, extra=2)

    if request.method == "POST":
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix="authors")
        book_formset = BooksFormSet(request.POST, request.FILES, prefix="books")
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy("p_library:author_list"))
    else:
        author_formset = AuthorFormSet(prefix = "authors")
        book_formset = BooksFormSet(prefix="books")
    return render(request, "manage_books_authors.html", {"author_formset": author_formset, 'book_formset': book_formset})

class BooksListView(ListView):
    template_name = 'books_list.html'
    context_object_name = "books"
    model = Book
    
class BookUpdateView(UpdateView):
    template_name = 'book_update.html'
    model = Book
    fields = ['friend', 'title', 'description', 'author', 'copy_count', 'price',]
    success_url = reverse_lazy("p_library:books_list")