from django.shortcuts import get_object_or_404
from book_forum.forms import BookForumForm, ReviewBookForm
from book_forum.models import Book_Forum
from django.views import generic


class BookListView(generic.ListView):
    template_name = 'crud/book_list.html'
    context_object_name = 'book'
    model = Book_Forum

    def __str__(self):
        return self.model.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'crud/book_detail.html'
    context_object_name = 'book_id'
    model = Book_Forum

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=book_id)


class CreateBookView(generic.CreateView):
    template_name = 'crud/create_book.html'
    form_class = BookForumForm
    success_url = '/book_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


class UpdateBookView(generic.UpdateView):
    template_name = 'crud/edit_book.html'
    form_class = BookForumForm
    success_url = '/book_list/'
    model = Book_Forum

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBookView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=book_id)


class DeleteBookView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/book_list/'
    model = Book_Forum

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=book_id)


class SearchBookView(generic.ListView):
    template_name = 'crud/book_list.html'
    context_object_name = 'book'
    paginate_by = '3'

    def get_queryset(self):
        query_param = self.request.GET.get('q')
        if query_param is not None:
            return Book_Forum.objects.filter(name__icontains=query_param)
        else:
            return Book_Forum.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class CommentCreateView(generic.CreateView):
    template_name = 'comment/create_comment.html'
    form_class = ReviewBookForm
    success_url = '/book_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CommentCreateView, self).form_valid(form=form)

# def create_book_forum_view(request):
#     if request.method == 'POST':
#         form = BookForumForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Book create successfully</h1>')
#     else:
#         form = BookForumForm()
#     return render(request, template_name='crud/create_book.html',
#                   context={'form': form})

# def book_list_view(request):
#     if request.method == 'GET':
#         book = Book_Forum.objects.all()
#         return render(request, template_name='crud/book_list.html',
#                       context={'book': book})

# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(Book_Forum, id=id)
#         return render(request, template_name='crud/book_detail.html',
#                       context={'book_id': book_id})

# def delete_book_forum_view(request, id):
#     book_id = get_object_or_404(Book_Forum, id=id)
#     book_id.delete()
#     return HttpResponse('<h1>Book deleted successfully</h1>')

# def edit_book_forum_view(request, id):
#     book_id = get_object_or_404(Book_Forum, id=id)
#     if request.method == 'POST':
#         form = BookForumForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Book is updated successfully</h1>')
#     else:
#         form = BookForumForm(instance=book_id)
#     return render(request, template_name='crud/edit_book.html',
#                   context={'form': form})
