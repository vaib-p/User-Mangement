# serializers.py

from rest_framework import serializers
from .models import User, Organization, Role, MembershipRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'organizations']

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'billing_group']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'organization']

class MembershipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipRequest
        fields = ['id', 'user', 'organization', 'status']
