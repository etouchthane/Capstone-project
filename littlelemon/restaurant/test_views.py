from datetime import timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Booking, Menu


class MenuViewTests(APITestCase):
	def setUp(self):
		self.menu_item = Menu.objects.create(Title='Pasta', Price='12.50', Inventory=20)

	def test_homepage_loads(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_menu_items_list_works(self):
		response = self.client.get('/api/menu-items/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertGreaterEqual(len(response.data), 1)


class BookingViewTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpass123')

	def test_booking_api_requires_auth(self):
		response = self.client.get('/api/bookings/')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_booking_api_with_auth(self):
		self.client.force_authenticate(user=self.user)
		payload = {
			'Name': 'John',
			'No_of_guests': 4,
			'BookingDate': (timezone.now() + timedelta(days=1)).isoformat(),
		}
		response = self.client.post('/api/bookings/', payload, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Booking.objects.count(), 1)

	def test_token_generation_endpoint(self):
		response = self.client.post('/api/api-token-auth/', {
			'username': 'testuser',
			'password': 'testpass123',
		})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn('token', response.data)
