# views.py

from django.http import Http404
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .models import User, Organization, Role, MembershipRequest
from .serializers import UserSerializer, OrganizationSerializer, RoleSerializer, MembershipRequestSerializer


# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Organization, Role, MembershipRequest
from .serializers import UserSerializer, OrganizationSerializer, RoleSerializer, MembershipRequestSerializer

class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Similarly implement views for other models (Organization, Role, MembershipRequest)



class OrganizationViewSet(views.APIView):
    def get(self, request):
        orinizations = Organization.objects.all()
        serializer = OrganizationSerializer(orinizations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoleViewSet(views.APIView):
    def get(self, request):
        Roles = Role.objects.all()
        serializer = RoleSerializer(Roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MembershipRequestViewSet(views.APIView):
    def get(self, request):
        Members = Members.objects.all()
        serializer = MembershipRequestSerializer(Members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MembershipRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
