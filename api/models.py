from django.db import models


class Coin(models.Model):
    denomination = models.IntegerField(unique=True)


class Good(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()


class MachineState(models.Model):
    coins = models.ManyToManyField(Coin, through='CoinQuantity')
    goods = models.ManyToManyField(Good)


class CoinQuantity(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    machine_state = models.ForeignKey(MachineState, on_delete=models.CASCADE)

