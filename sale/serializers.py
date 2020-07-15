from rest_framework import serializers

from sale.models import Advertisement, Offer


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
        read_only = ['owner']

    def create(self, validated_data):
        user = self.context['request'].user
        instance = Advertisement(owner=user, **validated_data)
        instance.save()
        return instance


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
        read_only = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        instance = Offer(user=user, **validated_data)
        instance.save()
        return instance
