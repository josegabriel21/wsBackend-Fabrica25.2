# meu_app/views.py
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer
import requests

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('nome')
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer

class BuscarReceitaView(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if not query:
            return Response(
                {"erro": "Parâmetro de busca 'q' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )

        external_api_url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={query}'
        try:
            response = requests.get(external_api_url)
            response.raise_for_status()
            data = response.json()
            return Response(data)
        except requests.exceptions.RequestException as e:
            return Response(
                {"erro": f"Não foi possível conectar à API de receitas: {e}"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )