from django.shortcuts import render, get_object_or_404
from book_forum.forms import BookForumForm
from book_forum.models import Book_Forum
from django.http import HttpResponse

def book_list_view(request):
    if request.method == 'GET':
        book = Book_Forum.objects.all()
        return render(request, template_name='crud/book_list.html',
                      context={'book': book})

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book_Forum, id=id)
        return render(request, template_name='crud/book_detail.html',
                      context={'book_id': book_id})

def edit_book_forum_view(request, id):
    book_id = get_object_or_404(Book_Forum, id=id)
    if request.method == 'POST':
        form = BookForumForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Book is updated successfully</h1>')
    else:
        form = BookForumForm(instance=book_id)
    return render(request, template_name='crud/edit_book.html',
                  context={'form': form})

def delete_book_forum_view(request, id):
    book_id = get_object_or_404(Book_Forum, id=id)
    book_id.delete()
    return HttpResponse('<h1>Book deleted successfully</h1>')

def create_book_forum_view(request):
    if request.method == 'POST':
        form = BookForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Book create successfully</h1>')
    else:
        form = BookForumForm()
    return render(request, template_name='crud/create_book.html',
                  context={'form': form})