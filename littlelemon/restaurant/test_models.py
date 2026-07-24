from django.test import TestCase

from .models import Menu, Booking


class MenuModelTests(TestCase):
	def setUp(self):
		self.menu_item = Menu.objects.create(
			Title='Pasta',
			Price='12.50',
			Inventory=20
		)

	def test_menu_creation(self):
		self.assertEqual(self.menu_item.Title, 'Pasta')
		self.assertEqual(str(self.menu_item.Price), '12.50')
		self.assertEqual(self.menu_item.Inventory, 20)

	def test_menu_str_representation(self):
		self.assertEqual(str(self.menu_item), 'Pasta')


class BookingModelTests(TestCase):
	def setUp(self):
		from django.utils import timezone
		self.booking = Booking.objects.create(
			Name='John Doe',
			No_of_guests=4,
			BookingDate=timezone.now()
		)

	def test_booking_creation(self):
		self.assertEqual(self.booking.Name, 'John Doe')
		self.assertEqual(self.booking.No_of_guests, 4)

	def test_booking_str_representation(self):
		self.assertEqual(str(self.booking), 'John Doe')
