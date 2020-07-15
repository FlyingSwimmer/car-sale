from django.contrib.auth.models import User
# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from sale.models import Advertisement, Offer


def create_test_user(username, password):
    return User.objects.create_user(username=username, password=password)


class ListCreateAdvertisementsViewTests(APITestCase):

    def test_create_advertisement(self):
        user = create_test_user('rahmat', '12345')
        self.client.force_login(user=user)
        url = reverse('list-create-advertisements')
        data = {
            'title': 'کچلیک',
            'description': 'شیمیک',
            'car_name': 'میمیک',
            'car_model': 'شیتیک',
            'min_price': 42,
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Advertisement.objects.count(), 1)
        self.assertEqual(Advertisement.objects.get().title, data['title'])
        self.assertEqual(Advertisement.objects.get().description, data['description'])
        self.assertEqual(Advertisement.objects.get().car_name, data['car_name'])
        self.assertEqual(Advertisement.objects.get().car_model, data['car_model'])
        self.assertEqual(Advertisement.objects.get().min_price, data['min_price'])

    def test_get_all_advertisements(self):
        data = {
            'owner': create_test_user('akbar', 'basir123'),
            'title': 'شلقم',
            'description': 'شلقم نابی',
            'car_name': 'شلقم',
            'car_model': '۱۳۸۵',
            'min_price': 46,
        }
        Advertisement.objects.create(**data)
        url = reverse('list-create-advertisements')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class CreateOfferTests(APITestCase):
    def test_create_offer(self):
        ad_data = {
            'owner': create_test_user('akbar', 'basir123'),
            'title': 'شلقم',
            'description': 'شلقم نابی',
            'car_name': 'شلقم',
            'car_model': '۱۳۸۵',
            'min_price': 46,
        }
        ad = Advertisement.objects.create(**ad_data)

        user = create_test_user('rahmat', '12345')
        self.client.force_login(user=user)
        url = reverse('add-offer')
        data = {
            'advertisement': ad.id,
            'price': 67,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Offer.objects.count(), 1)
        self.assertEqual(Offer.objects.get().advertisement.id, data['advertisement'])
        self.assertEqual(Offer.objects.get().price, data['price'])
        self.assertEqual(Offer.objects.get().user, user)
