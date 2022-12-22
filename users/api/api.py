from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework import viewsets



from users.tokens import create_jwt_pair_for_user
from users.models import Usuario
from users.api.serializers import UsuarioSerializer, LoginSerializer, SignUpSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer

    def list(self, request):

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def create(self, request):        
        return Response({"error":"No disponible"}, status = status.HTTP_204_NO_CONTENT)

    # def update(self, request, pk=None):
    #     return Response({"error":"Actualizado"}, status = status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        usuario = Usuario.objects.get(id=pk) 
        if usuario:
            usuario.is_active = False
            usuario.save()
            return Response({'message':"Usuario Eliminado con exito"}, status = status.HTTP_200_OK)
        return Response({'Error':"No se ha encontrado este usuario"}, status = status.HTTP_400_BAD_REQUEST)

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request:Request):
        print(request.data)
        data = request.data        
        serializer = self.serializer_class(data = data)
        
        if serializer.is_valid():
            serializer.save()            
            response = {"message":"Usuario creado correctamente", "data":serializer.data}
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request:Request):       
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)

            response ={"message":"Logueado Correctamente", "email":email, "tokens":tokens}
            return Response(data = response, status = status.HTTP_200_OK)
        return Response(data={"message":"Invalid email or incorrect password"})
    
    def get(self, request:Request):
        content = {"user":str(request.user), "auth":str(request.auth)}
        return Response(data=content, status = status.HTTP_200_OK)
