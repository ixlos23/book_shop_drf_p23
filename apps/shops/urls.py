from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shops.views import AddressListCreateAPIView, CountryListAPIView, AddressBookUpdateAPIView, AddressBookDeleteAPIView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('/address', AddressListCreateAPIView.as_view()),
    path('/address/<int:pk>', AddressBookUpdateAPIView.as_view()),
    path('/address/<int:pk>', AddressBookDeleteAPIView.as_view()),
    path('/country', CountryListAPIView.as_view()),
]