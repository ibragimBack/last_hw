from django.shortcuts import render
from book.models import Library

def post_library_view(request):
    if request.method == 'GET':
        query = Library.objects.all()
        return render(request, template_name='library.html',
                      context={'query': query})