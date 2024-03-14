from django.shortcuts import render, get_object_or_404
from book.models import Library

def post_library_view(request):
    if request.method == 'GET':
        query = Library.objects.all()
        return render(request, template_name='library.html',
                      context={'query': query})

def post_librarys_detail_view(request, id):
    if request.method == 'GET':
        query_id = get_object_or_404(Library, id=id)
        return render(request, template_name='library_detail.html',
                      context={'query_id': query_id})
