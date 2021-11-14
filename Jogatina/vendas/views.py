from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from .forms import createSaleAnnounce,createCompra
from .models import saleAnnounce, transactions

class saleAnnounceListView (ListView):
    model = saleAnnounce

class saleAnnounceDetailView (DetailView):
    model = saleAnnounce


def create_compra(request,ttitle):
    sale = saleAnnounce.objects.get(title=ttitle)
    form_buy = createCompra(request.POST)

    if request.method == 'POST':
        if form_buy.is_valid():
            buy = form_buy.save(commit = False)
            buy.vendor = sale.vendor
            buy.customer = request.user
            buy.price = sale.price
            sale.quatity = sale.quatity - 1
            sale.save()
            if sale.quatity == 0:
                sale.delete()
            buy.save()
            return redirect('vendas:list')


    context = {'form_buy' : form_buy, 'sale' : sale}
    return render(request, 'vendas/compra.html',context)

def create_SaleAnnounce(request):

    form = createSaleAnnounce(request.POST)

    if form.is_valid():
        sale = form.save(commit=False)
        sale.slug = sale.title
        sale.vendor = request.user
        sale.save()
        return redirect('vendas:list')

    return render(request, 'vendas/saleannounce_form.html', {'form' : form})

class transactionsListView (ListView):
    model = transactions

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'vendas/signup.html'