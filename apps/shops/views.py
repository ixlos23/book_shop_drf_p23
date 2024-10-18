from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated


from users.serializers import AddressListModelSerializer


# @extend_schema(tags=['users'])
# class AddressListCreateAPIView(ListCreateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressListModelSerializer
#     permission_classes = IsAuthenticated,
#
#     def get_queryset(self):
#         return super().get_queryset().filter(user=self.request.user)
#
#
# @extend_schema(tags=['users'])
# class CountryListAPIView(ListAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountryModelSerializer
#     authentication_classes = ()


# @extend_schema(tags=['users'])
# class AddressBookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressModelSerializer

# @extend_schema(tags=['users'])
# class AddressBookUpdateAPIView(UpdateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressModelSerializer
#
#
# @extend_schema(tags=['users'])
# class AddressBookDeleteAPIView(DestroyAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressModelSerializer
