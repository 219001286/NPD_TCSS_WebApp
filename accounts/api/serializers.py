from accounts.models import CustomUser
from rest_framework import serializers


class AccountRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    collector_spot = serializers.StringRelatedField()
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'gender', 'telephone', 'Id_number', 'email','collector_spot',
                  'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}    
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords must be the same'})

        if CustomUser.objects.filter(email=self.validated_data['email']):
            raise serializers.ValidationError({'error': 'Your email has already been taken'})

        if CustomUser.objects.filter(telephone=self.validated_data['telephone']):
            raise serializers.ValidationError({'error': 'This telephone has already been used'})

        account = CustomUser(first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'],
                                gender=self.validated_data['gender'], telephone=self.validated_data['telephone'],
                                Id_number=self.validated_data['Id_number'], 
                                email=self.validated_data['email'])
        account.set_password(password)
        account.save()
        return account