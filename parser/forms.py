from django import forms
from . import models, houses, news_parser
from parser.houses import get_html, MAIN_URL

class ParserSiteForm(forms.Form):
    MEDIA_CHOICES = (
        ('house.kg', 'house.kg'),
        ('24.kg', '24.kg')
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type']

    def parser_data(self):
        if self.data['media_type'] == 'house.kg':
            house_parser = houses.get_house_data(get_html(MAIN_URL))
            for i in house_parser:
                models.HousesParser.objects.create(**i)
        elif self.data['media_type'] == '24.kg':
            news_parsers = news_parser.parsing()
            for i in news_parsers:
                models.NewsParser.objects.create(**i)