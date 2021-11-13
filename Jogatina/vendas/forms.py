import datetime
from django.forms import ModelForm
from vendas.models import saleAnnounce

class createSaleAnnounce(ModelForm):

    class Meta:
        model = saleAnnounce
        fields = ['title','description','state','quatity','price']

