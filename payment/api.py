from rest_framework import viewsets
from .pagination import StandardResultsSetPagination
from .serializers import ServiceSerializer
from rest_framework import viewsets, filters 
from payment.models import Service

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['name']
    ordering = ('-id')