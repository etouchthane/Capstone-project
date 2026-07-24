from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


def index(request):
	return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
	return Response({"message": "This view is protected"})
