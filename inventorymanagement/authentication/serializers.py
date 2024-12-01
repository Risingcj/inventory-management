from rest_framework import serializers
from .models import User

# class SignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'role']
#         extra_kwargs = {
#             'password': {'write_only': True},
#             'role': {'required': True},
#         }

#     def create(self, validated_data):
#         # Create a new user with a hashed password
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password'],
#             role=validated_data['role']
#         )
#         return user

class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, help_text="Unique username for the user.")
    email = serializers.EmailField(required=True, help_text="Email address of the user.")
    password = serializers.CharField(write_only=True, required=True, help_text="Password for the user.")
    role = serializers.ChoiceField(
        choices=User.ROLE_CHOICES,
        required=True,
        help_text="Role of the user (e.g., 'staff', 'manager', 'admin')."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']