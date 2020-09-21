from rest_framework import serializers
from offers.models import OffersAd



class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffersAd
        fields = ['id', 'property_name', 'area', 'url', 'image_url', 'category','description','contact_number','date_published','date_expired']