from django.views import generic
from django.http import HttpResponse
from . import models, forms


class GetParsing(generic.FormView):
    template_name = 'parsers/get_parsing.html'
    form_class = forms.ParserSiteForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Parsing successful</h1>')
        else:
            return super(GetParsing, self).post(request, *args, **kwargs)


class HouseListView(generic.ListView):
    template_name = 'parsers/house_list.html'
    model = models.HousesParser
    context_object_name = 'houses'

    def get_queryset(self):
        return self.model.objects.all()


class NewListView(generic.ListView):
    template_name = 'parsers/news_list.html'
    model = models.NewsParser
    context_object_name = 'news'

    def get_queryset(self):
        return self.model.objects.all()
