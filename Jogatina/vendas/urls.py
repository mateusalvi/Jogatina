from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "vendas"

urlpatterns = [
    path("", views.saleAnnounceListView.as_view(), name="list"),
    path("<slug:slug>/", views.saleAnnounceDetailView.as_view(), name="detail"),
]
