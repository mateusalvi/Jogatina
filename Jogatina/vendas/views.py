from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import saleAnnounce

class saleAnnounceListView (ListView):
    model = saleAnnounce

class saleAnnounceDetailView (DetailView):
    model = saleAnnounce