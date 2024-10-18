from django.urls import path


from users.views import UserUpdateAPIView, RegisterCreateAPIView, LoginAPIView, \
    UserWishlistCreateAPIViewDestroyAPIView, ActivateUserView, AddressDestroyUpdateAPIView, AddressListCreateAPIView, \
    CountryListAPIView

urlpatterns = [
    path('address', AddressListCreateAPIView.as_view(), name='address_list'),
    path('country', CountryListAPIView.as_view()),
    path('update-user', UserUpdateAPIView.as_view()),

    path('address/<int:pk>', AddressDestroyUpdateAPIView.as_view(), name='address_detail'),
    path('register', RegisterCreateAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('activate/<uidb64>/<token>', ActivateUserView.as_view(), name='activate'),

]