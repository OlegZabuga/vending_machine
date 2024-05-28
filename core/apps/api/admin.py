from django.contrib import admin
from .models import Coin, Good, MachineState, CoinQuantity

admin.site.register(Coin)
admin.site.register(Good)
admin.site.register(MachineState)
admin.site.register(CoinQuantity)
