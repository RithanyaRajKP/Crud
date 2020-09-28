import django_filters
from . models import Students

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model= Students
        fields ='__all__'
