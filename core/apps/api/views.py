from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import Good, Coin, MachineState
from .serializers import GoodSerializer, CoinSerializer, MachineStateSerializer, UserSerializer

class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        # Логика покупки товара
        pass

class ChargeViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def charge(self, request):
        # Логика пополнения денег
        pass

class StatusViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def status(self, request):
        # Логика получения статуса
        pass

class DischargeViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def discharge(self, request):
        # Логика выдачи сдачи
        pass

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        from django.contrib.auth import authenticate
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class ServiceViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def list_goods_and_coins(self, request):
        # Логика получения списка товаров и монет
        pass

    @action(detail=False, methods=['post'])
    def restock(self, request):
        # Логика пополнения товаров и монет
        pass
