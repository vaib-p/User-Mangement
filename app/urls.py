# urls.py

from django.urls import path
from .views import UserListCreateAPIView, UserDetailAPIView,OrganizationViewSet,RoleViewSet,MembershipRequestViewSet

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('organizations/', OrganizationViewSet.as_view(), name='organization-list-create'),
    path('roles/', RoleViewSet.as_view(), name='role-list-create'),
    path('membership-requests/', MembershipRequestViewSet.as_view(), name='membership-request-list-create'),
]
