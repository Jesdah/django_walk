from django import fores
from .models import Item



class ItemForm(forms.ModelForms):
    class Meta:
        model = Item
        fields = ['name', 'done']