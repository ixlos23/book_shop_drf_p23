from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from shops.models import Address, Country


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AddressModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Address
        fields = '__all__'

    def to_representation(self, instance: Address):
        repr = super().to_representation(instance)
        repr['country'] = CountryModelSerializer(instance.country).data
        return repr


    def validate(self, attrs):
        default_billing_address = attrs.get('billing_address')
        default_shipping_address = attrs.get('shipping_address')
        if default_billing_address or default_shipping_address:
            return attrs
