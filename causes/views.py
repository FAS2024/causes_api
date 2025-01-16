from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .models import Cause, Contribution
from .serializers import CauseSerializer, ContributionSerializer
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response

# views.py
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.serializers import Serializer, CharField




def welcome_view(request):
    return JsonResponse({
        "message": "Welcome to the Causes API.",
        "endpoints": {
            "list_causes": "/api/causes/",
            "create_cause": "/api/causes/",
            "retrieve_update_delete_cause": "/api/causes/{id}/",  # Use placeholder for 'id'
            "contribute_to_cause": "/api/causes/{id}/contribute/"  # Use placeholder for 'id'
        }
    })



class CauseViewSet(viewsets.ModelViewSet):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return Cause.objects.get(pk=self.kwargs['pk'])
        except Cause.DoesNotExist:
            raise NotFound(detail="Cause not found.")

    @action(detail=True, methods=['post'], url_path='contribute')
    def contribute(self, request, pk=None):
        cause = self.get_object()  # Ensure the cause exists
        serializer = ContributionSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure that the contribution is valid
            serializer.save(cause=cause)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Create a simple registration serializer
class RegisterSerializer(Serializer):
    username = CharField(max_length=100)
    password = CharField(max_length=100)

# Create a simple registration view
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow anyone to access this endpoint

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Create the user
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = User.objects.create_user(username=username, password=password)
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
