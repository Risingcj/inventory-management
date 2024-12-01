# from rest_framework import serializers
# from .models import User
# from django.db import IntegrityError

# # class SignupSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = ['username', 'email', 'password', 'role']
# #         extra_kwargs = {
# #             'password': {'write_only': True},
# #             'role': {'required': True},
# #         }

# #     def create(self, validated_data):
# #         # Create a new user with a hashed password
# #         user = User.objects.create_user(
# #             username=validated_data['username'],
# #             email=validated_data['email'],
# #             password=validated_data['password'],
# #             role=validated_data['role']
# #         )
# #         return user

# # class SignupSerializer(serializers.ModelSerializer):
# #     username = serializers.CharField(required=True, help_text="Unique username for the user.")
# #     email = serializers.EmailField(required=True, help_text="Email address of the user.")
# #     password = serializers.CharField(write_only=True, required=True, help_text="Password for the user.")
# #     role = serializers.ChoiceField(
# #         choices=User.ROLE_CHOICES,
# #         required=True,
# #         help_text="Role of the user (e.g., 'staff', 'manager', 'admin')."
# #     )

# #     class Meta:
# #         model = User
# #         fields = ['username', 'email', 'password', 'role']

# from rest_framework import serializers
# from .models import User

# class SignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'role']
#         extra_kwargs = {
#             'password': {'write_only': True},
#             'role': {'required': True},
#         }

#     def validate_username(self, value):
#         if User.objects.filter(username=value).exists():
#             raise serializers.ValidationError("A user with this username already exists.")
#         return value

#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("A user with this email already exists.")
#         return value

#     def create(self, validated_data):
#         try:
#             return User.objects.create_user(
#                 username=validated_data['username'],
#                 email=validated_data['email'],
#                 password=validated_data['password'],
#                 role=validated_data['role']
#             )
#         except IntegrityError:
#             raise serializers.ValidationError("A user with this username or email already exists.")
from rest_framework import serializers
from django.db import IntegrityError
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'required': True},
        }

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        try:
            # Use `create_user` to ensure password is hashed
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                role = validated_data.get('role', 'staff')  # Default to 'staff'
            )
            return user
        except IntegrityError:
            raise serializers.ValidationError("A user with this username or email already exists.")
