from .models import User, Transaction
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, TransactionSerializer


 # User viewsets

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = UserSerializer

# Transactions viewsets

class TransactionViewSet(viewsets.ModelViewSet):
	queryset = Transaction.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = TransactionSerializer


