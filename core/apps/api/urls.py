from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api import views

router = DefaultRouter()
router.register(r'goods', views.GoodViewSet)
router.register(r'charge', views.ChargeViewSet, basename='charge')
router.register(r'status', views.StatusViewSet, basename='status')
router.register(r'discharge', views.DischargeViewSet, basename='discharge')
router.register(r'service', views.ServiceViewSet, basename='service')
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]