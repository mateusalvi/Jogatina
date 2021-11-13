from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.template.defaultfilters import slugify
# Create your models here.

ESTADO = (
    ('novo','Novo'),
    ('usado','Usado'),
)

class saleAnnounce (models.Model): #banco de dados de anúncios de vendas
    title = models.CharField(max_length=255) #nome do anúncio
    slug = models.SlugField(max_length=255, unique=True) #nome do url unico de cada venda
    vendor = models.ForeignKey(User, on_delete=models.CASCADE) #usuário que iniciou uma venda
    description = models.TextField() #texto descritivo do anuncio
    state = models.CharField(max_length=5, choices=ESTADO, default='novo')
    quatity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2) #valor máximo de uma carta é 10 mi
    date_announced = models.DateField(auto_now_add=True) #data do anúncio

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("vendas:detail", kwargs={'slug': self.slug})
        
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(saleAnnounce, self).save(*args, **kwargs)
