from django.forms import ModelForm
from vendas.models import saleAnnounce,transactions

class createSaleAnnounce(ModelForm):

    class Meta:
        model = saleAnnounce
        fields = ['title','description','state','quatity','price']

class createCompra(ModelForm):
    class Meta:
        model = transactions
        fields = []
