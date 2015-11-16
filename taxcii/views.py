# -*- coding: utf-8 -*-
from taxlib.ja.consumptiontax import ConsumptionTax
from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class ConsumptionTaxView(APIView):
    def get(self, request):
        pass
