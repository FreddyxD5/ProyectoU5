import random
from rest_framework import viewsets, status
from rest_framework.decorators import action
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

    @action(methods=['get'], detail=False, url_path='pagos', permission_classes=[IsAuthenticated])
    def obtener_pagos(self, request, pk=None):        
        # print(request.user.is_staff)
        if request.user.is_staff:
            queryset = PaymentUser.objects.order_by('id') 
        else:            
            queryset = PaymentUser.objects.filter(user=request.user.id)
            
        if queryset:
            datos_serializados = self.get_serializer(queryset, many=True)
            return Response(datos_serializados.data, status=status.HTTP_200_OK)
        return Response({'error':datos_serializados.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        request.data['user'] = request.user.id
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
            return Response({'message':"Registro creado satisfactoriamente."}, status = status.HTTP_201_CREATED)                
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)    
   

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

    @action(methods=['get'], detail=False, url_path='recibos_vencidos', permission_classes=[IsAuthenticated])
    def obtener_recibos_vencidos(self, request, pk=None):        
        # print(request.user.is_staff)
        if request.user.is_staff:
            queryset = ExpiredPayment.objects.order_by('id') 
        else:            
            queryset = ExpiredPayment.objects.filter(user=request.user.id).order_by('id')
            
        if queryset:
            datos_serializados = self.get_serializer(queryset, many=True)
            return Response(datos_serializados.data, status=status.HTTP_200_OK)
        return Response({'error':datos_serializados.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        return Response({"error":"Metodo no permitido, debe especificar un ID expired_payment/{id}"}, status=status.HTTP_204_NO_CONTENT)

    # def list(self, request):
    #     if self.queryset:
    #         serializer = self.get_serializer(self.get_queryset(), many=True)
    #         return Response(serializer.data, status = status.HTTP_200_OK)
    #     return Response({"message":"Aun no hay datos que mostrar"}, status=status.HTTP_204_NO_CONTENT)    


