from django.urls import path, include
from rest_framework import routers
from . import views

stock_router = routers.SimpleRouter()
stock_router.register('stock', views.StockViewSet)

app_name = "datasetapi"

urlpatterns = [
    path('', include(stock_router.urls)),
]