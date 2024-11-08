from django.urls import path

from users.views import AddressListCreateAPIView, RegisterCreateAPIView, LoginAPIView, UserActivateAPIView, \
    AddressDestroyUpdateAPIView, UserUpdateAPIView, UserWishlistCreateAPIViewDestroyAPIView, AuthorDetailView

urlpatterns = [
    path('address', AddressListCreateAPIView.as_view(), name='address_list'),
    path('address/<int:pk>', AddressDestroyUpdateAPIView.as_view(), name='address_detail'),
    path('update-user', UserUpdateAPIView.as_view(), name='update-user'),
    path('user-wishlist', UserWishlistCreateAPIViewDestroyAPIView.as_view(), name='wishlist-user'),

    path('register', RegisterCreateAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('activate/<str:uidb64>/<str:token>', UserActivateAPIView.as_view(), name='activate_user'),
    path('authors/<int:id>/', AuthorDetailView.as_view(), name='author-detail'),

]


