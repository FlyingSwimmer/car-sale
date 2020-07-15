# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from sale.models import Advertisement, Offer
from sale.serializers import AdvertisementSerializer, OfferSerializer


class ListCreateAdvertisement(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CreateOffer(generics.CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (IsAuthenticated,)
