from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


from .models import Coin, Good, MachineState, CoinQuantity

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['denomination']


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'name', 'price', 'quantity']


class CoinQuantitySerializer(serializers.ModelSerializer):
    coin = CoinSerializer()

    class Meta:
        model = CoinQuantity
        fields = ['coin', 'quantity']


class MachineStateSerializer(serializers.ModelSerializer):
    coins = CoinQuantitySerializer(many=True)
    goods = GoodSerializer(many=True)

    class Meta:
        model = MachineState
        fields = ['coins', 'goods']