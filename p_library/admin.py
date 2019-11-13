from django.contrib import admin
from p_library.models import Book, Author, Redaction, Friend

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author_admin")
    fields = (('ISBN', 'redaction'), 'year_release', 'author', 'title', 'description', 'price', 'copy_count', 'friend')

    @staticmethod
    def author_admin(obj):
        return "%s (%s)"%(obj.author.full_name, obj.author.country)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("country",)
    pass
@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendRegister(admin.ModelAdmin):
    pass