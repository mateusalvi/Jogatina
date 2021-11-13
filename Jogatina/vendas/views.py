from django.shortcuts import render
from django.views.generic import DetailView, ListView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from .forms import createSaleAnnounce
from .models import saleAnnounce

class saleAnnounceListView (ListView):
    model = saleAnnounce

class saleAnnounceDetailView (DetailView):
    model = saleAnnounce


def create_SaleAnnounce(request):

    form = createSaleAnnounce(request.POST)

    if form.is_valid():
        sale = form.save(commit=False)
        sale.slug = sale.title
        sale.vendor = request.user
        sale.save()
        return redirect('vendas:list')

    return render(request, 'vendas/saleannounce_form.html', {'form' : form})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'vendas/signup.html'