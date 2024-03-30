from django.shortcuts import render
from django.utils import timezone

from . import models, serializers
from .utilities import import_stock_csv_to_db

from rest_framework.permissions import AllowAny
from rest_framework import mixins, viewsets
from rest_framework.response import Response

import os

# Create your views here.
class StockViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
    Manage the goods in Stock
    """
    permission_classes = [AllowAny,]
    serializer_class = serializers.StockSerializer
    queryset = models.Stock.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self, *args, **kwargs):
        return models.Stock.objects.all()

    def list(self, request):
        cwd = os.getcwd()
        import_stock_csv_to_db(cwd + "\datasetapi\static\cleaned_data.csv")  # load csv into database
        qs = self.get_queryset()
        serializer = serializers.StockSerializer(qs, many=True)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(last_updated=timezone.now())
