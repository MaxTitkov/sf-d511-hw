from django import forms
from p_library.models import Author, Book

class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)
    class Meta:
        fields = "__all__"
        model = Author

    
class BookForm(forms.ModelForm):
    class Meta:
        fields="__all__"
        model=Book