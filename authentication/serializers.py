from rest_framework import serializers 
from users.models import *
from rest_framework.serializers import ValidationError

def Valid_username(username):
    if User.objects.filter(username=username).exists():
        raise ValidationError('This User Already Exisits')
    return username

def Valid_email(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError('This Email Already Exisits')
    return email
    
def Valid_strong_password(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must have at least 1 digit")
    if not any(char.isalpha() for char in password):
        raise ValidationError("Password must have at least 1 letter")
    if not any(char.isupper() for char in password):
        raise ValidationError("Password must have at least 1 uppercase letter")
    return password

def Valid_password(self):
    if not self['password'] or not self['confirm_password']:
        raise ValidationError("You Should Entre A Password")

    if self['password'] != self['confirm_password']:
        raise ValidationError("Passwords are not matched")

    return self['password']    



class AutenticationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 255 , required=True, validators = [Valid_username])
    email = serializers.EmailField(max_length = 255 , required=True, validators = [Valid_email])
    password = serializers.CharField(max_length = 255 , required = True , validators = [Valid_strong_password] , style = {'input_type': 'password'})
    confirm_password = serializers.CharField(max_length = 255 , required = True , style = {'input_type': 'password'})
    bio = serializers.CharField(max_length = 256 , required = False)
    class Meta:
        model = User
        fields = ['id' , 'username' , 'email' , "password" ,'confirm_password' , 'bio'] 
        validators = [Valid_password]
