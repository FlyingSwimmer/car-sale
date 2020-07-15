from django.urls import path

from sale.views import ListCreateAdvertisement, CreateOffer

urlpatterns = [
    path('advertisements', ListCreateAdvertisement.as_view(), name='list-create-advertisements'),
    path('offers/add', CreateOffer.as_view(), name='add-offer'),
]