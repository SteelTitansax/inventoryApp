from django.forms import ModelForm 
from .models import Item,Location

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name','person','location', 'comments']


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['location']