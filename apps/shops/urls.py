from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import AddressListCreateAPIView, AddressDestroyUpdateAPIView

router = DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),

    # path('country', CountryListAPIView.as_view()),
]