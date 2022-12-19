from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from payment.pagination import StandardResultsSetPagination
from payment.serializers import ServiceSerializer, PaymentUserSerializer, ExpiredPaymentSerializer
from payment.models import Service, PaymentUser, ExpiredPayment


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ('name',)
    permission_classes=[IsAuthenticated]

    search_fields = ['name']
    ordering = ('-id')

    throttle_scope = 'services'



class PaymentUserViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentUserSerializer
    queryset = PaymentUser.objects.all().order_by('id')
    permission_classes=[IsAuthenticated] 
    pagination_class = StandardResultsSetPagination

    filter_backends = [filters.DjangoFilterBackend]    
    # filterset_fields = ('user','payment_date', 'expiration_date',)

    throttle_scope = 'payments'

    class Meta:
        ordering = ['-id']

    def list(self, request):        
        if self.queryset:
            serializer = self.get_serializer(self.get_queryset(), many=True)        
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response({"message":"Aun no hay datos que mostrar"}, status=status.HTTP_203_NO_CONTENT)

class ExpiredPaymentViewSet(viewsets.ModelViewSet):
    serializer_class = ExpiredPaymentSerializer
    queryset = ExpiredPayment.objects.all().order_by('id')
    permission_classes=[IsAuthenticated] 
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]    
    # filterset_fields = ('user','payment_date', 'service',)
    throttle_scope = 'expired'


    class Meta:
        ordering = ['-id']

    def list(self, request):
        if self.queryset:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({"message":"Aun no hay datos que mostrar"}, status=status.HTTP_203_NO_CONTENT)
        

