from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer ,TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


from .models import User, Transaction


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'})
    user = authenticate(username= username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'})
    S = User.objects.get(RIB = username)
    serializer =UserSerializer(S,many=False)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,'id' : serializer.data['id']})

@csrf_exempt
@api_view(['GET'])

def apiOverView(request):
	api_urls = {
		'MoneySent':'/sentmoney/<str:id>',
		'User' : '/user/<str:key>',
		'Moneyrecieved' :  '/recievedmoney/<int:id>',
		'CreateUser' : '/user/',
		'MakeTransaction' : '/transaction/',
		'update':'/user/<int:id>',
		'login': '/login/',
	}
	return Response(api_urls)

@csrf_exempt
@api_view(['GET'])
def MoneySent(request , id) :
	S = Transaction.objects.filter(SenderId = id)
	serializer = TransactionSerializer(S , many=True)
	return Response(serializer.data)
@csrf_exempt
@api_view(['GET'])
def getUser(request , key):

	S = User.objects.get(id = key)
	serializer = UserSerializer(S , many=False)
	return Response(serializer.data)
@csrf_exempt
@api_view(['GET'])
def MoneyReceived(request , id):
	S = Transaction.objects.filter(RecieverId = id)
	serializer = TransactionSerializer(S , many=True)
	return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def MakeTansaction(request):
	serializer = TransactionSerializer(data = request.data)
	print(type(request.data))
	if serializer.is_valid() :
		serializer.save()

	
	R = serializer.data['RecieverId']
	S  = serializer.data['SenderId']
	amount = serializer.data['amount']
	rec = User.objects.get(id = R )
	sen = User.objects.get(id = S )
	rec.balance = rec.balance + amount
	sen.balance = sen.balance - amount
	rec.save()
	sen.save()
	


	return Response(serializer.data)

# Create your views here.
