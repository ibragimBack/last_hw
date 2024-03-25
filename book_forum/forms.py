from django import forms
from book_forum.models import Book_Forum, ReviewBook

class BookForumForm(forms.ModelForm):
    class Meta:
        model = Book_Forum
        fields = '__all__'

class ReviewBookForm(forms.ModelForm):
    class Meta:
        model = ReviewBook
        fields = '__all__'