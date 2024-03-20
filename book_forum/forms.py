from django import forms
from book_forum.models import Book_Forum

class BookForumForm(forms.ModelForm):
    class Meta:
        model = Book_Forum
        fields = '__all__'