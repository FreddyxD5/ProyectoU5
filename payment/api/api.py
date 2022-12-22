import random
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from payment.pagination import StandardResultsSetPagination
from payment.api.serializers import ServiceSerializer, PaymentUserSerializer, ExpiredPaymentSerializer
from payment.models import Service, PaymentUser, ExpiredPayment
from payment.permissions import CustomPermission, CustomPaymentUserPermission

from payment.filters import PaymentUserFilter

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer
    permission_classes = [CustomPermission]

    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, )    
    filterset_fields = {
        'name':['contains']
    }
    

    search_fields = ['name']
    ordering = ('-id')

    throttle_scope = 'services'



class PaymentUserViewSet(viewsets.ModelViewSet):
    queryset = PaymentUser.objects.all().order_by('id')
    serializer_class = PaymentUserSerializer    
    permission_classes=[CustomPaymentUserPermission]

    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, )    
    filterset_class = PaymentUserFilter
    throttle_scope = 'payments'

    class Meta:
        ordering = ['-id']

    def create(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            payment_user = PaymentUser(
                    user = serializer.validated_data['user'],
                    service= serializer.validated_data['service'],
                    amount= serializer.validated_data['amount'],
                    payment_date= serializer.validated_data['payment_date'],
                    expiration_date= serializer.validated_data['expiration_date'],
                    )
            payment_user.save()
            #Creacion de Registro ExpiredPayment
            if serializer.validated_data['payment_date'] > serializer.validated_data['expiration_date']:                                            
                ExpiredPayment.objects.create(payment_user=payment_user)
                return Response({'message':"Registro creado satisfactoriamente."}, status = status.HTTP_201_CREATED)                
        return Response({'error':"Por favor asegurese de que los datos sean correctos."}, status = status.HTTP_400_BAD_REQUEST)    
   

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

