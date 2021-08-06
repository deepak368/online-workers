
from .models import userRequest
import django_filters



class Search_work(django_filters.FilterSet):
    class Meta:
        model=userRequest
        fields=['Work_type']