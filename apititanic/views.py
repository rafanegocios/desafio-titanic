from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apititanic.service.csv_handler import CSVHandler
from apititanic.serializers import SurvivalSerializers
# Create your views here.

class SummaryView(APIView):
    """ Exibe um resumo estatístico da tabela de sobreviventes do titanic """
    def get(self, request, format=None):
        handler = CSVHandler('apititanic/data/train.csv')
        data = handler.get_summary()
        res = {
            'status' : 'success',
            'data' : data
        }
        return Response(res)
    

class SurvivalRateView(APIView):
    """ Exibe a taxa de sobrevivência global do titanic """
    def get(self,request,format=None):
        handler = CSVHandler('apititanic/data/train.csv')
        data = handler.get_survival()
        res = {
            'status' : 'sucess',
            'data' : {'survival_rate':data}
        }
        return Response(res)
    
class AverageSurvivalRateView(APIView):
    """ 
    Exibe a taxa de sobrevivência média agrupada por
    uma coluna específica ou Geral
    """
    def get(self, request,column, format=None):
        if not column:
            return Response(
                {"error": "O parâmetro 'column' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            handler = CSVHandler('apititanic/data/train.csv')
            data = handler.get_average_survival_rate(column)  # Chamar função passando a coluna
            res = {
                'status':'success',
                'column':column,
                'taxa_media_de_sobrevivencia':data
            }
            return Response(res)
        
        except KeyError:
            return Response(
                {"error": f"A coluna '{column}' não existe na base de dados."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
class CleanDataView(APIView):
    """Recebe os dados em JSON pela requisição e exibe o retorno desses dados com tratamento adequado"""
    def post(self, request, format=None):
        serializer = SurvivalSerializers(data=request.data,many=True)
        if serializer.is_valid():
            handler = CSVHandler('apititanic/data/train.csv')
            data = handler.post_clean_data(serializer.data)
            res={
                'status':'success',
                'data':data
            }
            return Response(res)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CorrelationView(APIView):
    """ 
    Exibe a matriz de correlação entre as variáveis
    numéricas, o que ajuda a entender quais variáveis podem ter uma
    relação forte entre si
    """
    def get(self,request,format=None):
        handler = CSVHandler('apititanic/data/train.csv')
        data = handler.get_correlation()
        res={
            'status':'success',
            'matrix':data
        }
        return Response(res)