from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from users.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = []
        read_only_fields = 'created_at',

    def to_representation(self, instance):
        return {
            "id":instance.id,
            "email": instance.email,
            "nombres":instance.nombres if instance.nombres is not None else '',
            "apellidos":instance.apellidos if instance.apellidos is not None else '',
            "telefono":instance.telefono if instance.telefono is not None else '',
            "direccion":instance.direccion if instance.direccion is not None else ''            
        }
    
class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)      
    password1 = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Usuario
        fields = ['email','password1', 'password2']

    
    def validate(self, attrs):
        email_exists = Usuario.objects.filter(email =attrs['email']).exists()
        if email_exists:
            raise ValidationError("El email ya ha sido usado")
        return super().validate(attrs)

    def create(self, validated_data):
        password1 = validated_data.pop('password1')
        password2 = validated_data.pop('password2')
        user = super().create(validated_data)
        if password1 != password2:
            raise ValidationError("Las contraseñas deben ser iguales")
        user.set_password(password1)
        user.save()        
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = Usuario
        fields = ['username','password']