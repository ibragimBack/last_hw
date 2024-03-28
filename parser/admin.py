from django.contrib import admin
from . models import HousesParser, NewsParser

admin.site.register(HousesParser)
admin.site.register(NewsParser)