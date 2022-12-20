from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from payment.pagination import StandardResultsSetPagination
from payment.api.serializers import ServiceSerializer, PaymentUserSerializer, ExpiredPaymentSerializer
from payment.models import Service, PaymentUser, ExpiredPayment
from payment.permissions import CustomPermission, CustomPaymentUserPermission


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, )
    search_fields = ['name']
    filterset_fields = ('name',)
    permission_classes = [CustomPermission]

    search_fields = ['name']
    ordering = ('-id')

    throttle_scope = 'services'



class PaymentUserViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentUserSerializer
    queryset = PaymentUser.objects.all().order_by('id')
    permission_classes=[CustomPaymentUserPermission] 
    pagination_class = StandardResultsSetPagination

    filter_backends = (filters.DjangoFilterBackend, )
    search_fields = ['user']
    filterset_fields = ('user','payment_date', 'expiration_date',)

    throttle_scope = 'payments'

    class Meta:
        ordering = ['-id']

    def list(self, request):        
        if self.queryset:
            serializer = self.get_serializer(self.get_queryset(), many=True)        
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response({"message":"Aun no hay datos que mostrar"}, status=status.HTTP_204_NO_CONTENT)

class ExpiredPaymentViewSet(viewsets.ModelViewSet):
    serializer_class = ExpiredPaymentSerializer
    queryset = ExpiredPayment.objects.all().order_by('id')
    permission_classes=[CustomPermission] 
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, )   
    filterset_fields = ('payment_user',)
    throttle_scope = 'expired'


    class Meta:
        ordering = ['-id']

    def list(self, request):
        return Response({"error":"Metodo no permitido, debe especificar un ID expired_payment/{id}"}, status=status.HTTP_204_NO_CONTENT)

    # def list(self, request):
    #     if self.queryset:
    #         serializer = self.get_serializer(self.get_queryset(), many=True)
    #         return Response(serializer.data, status = status.HTTP_200_OK)
    #     return Response({"message":"Aun no hay datos que mostrar"}, status=status.HTTP_204_NO_CONTENT)    

    def create(self, request):
        return Response({"Payment Expired":"Creado correctamente"}, status=status.HTTP_201_CREATED)
        

    def retrieve(self, request, pk=None):
        return Response({"datos":"Datos del registro"}, status=status.HTTP_200_OK)

