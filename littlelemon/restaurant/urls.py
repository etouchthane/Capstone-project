from django.urls import path
from django.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='home'),
    path('api/menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('api/menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api/message/', views.msg, name='protected-message'),
    path('api/api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('api/', include(router.urls)),
]