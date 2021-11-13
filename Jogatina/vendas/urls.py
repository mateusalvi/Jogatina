from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "vendas"

urlpatterns = [
    path('create/', views.create_SaleAnnounce, name='createSaleAnnounce'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path("", views.saleAnnounceListView.as_view(), name="list"),
    path("<slug:slug>/", views.saleAnnounceDetailView.as_view(), name="detail"),
    
   
]
