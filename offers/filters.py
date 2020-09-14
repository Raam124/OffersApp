import django_filters
from offers.models import OffersAd


class OffersFilter(django_filters.FilterSet):

    category  = django_filters.AllValuesFilter( widget=django_filters.widgets.LinkWidget(), field_name="category", label="Category")

    class Meta:
        model = OffersAd
        fields = ['category']