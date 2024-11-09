from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apititanic.service.csv_handler import CSVHandler
# Create your views here.

class SummaryView(APIView):
    def get(self, request, format=None):
        handler = CSVHandler('apititanic/data/train.csv')
        data = handler.get_summary()
        res = {
            'status' : 'success',
            'data' : data
        }
        return Response(res)
    

class SurvivalRateView(APIView):
    def get(self,request,format=None):
        handler = CSVHandler('apititanic/data/train.csv')
        data = handler.get_survival()
        res = {
            'status' : 'sucess',
            'data' : {'survival_rate':data}
        }
        return Response(res)