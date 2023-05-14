from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework import permissions

from app.models import Persion, Cars
from app.serializers import PersionModelSerilizers, CarsModelSerilizers

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework import filters

# Create your views here.


class GetAllData(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        query = Persion.objects.all()
        serializers = PersionModelSerilizers(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # def put(self, request, pk):
    #     query = Persion.objects.get(pk=pk)
    #     serializers = PersionModelSerilizers(query, data=request.data)

    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data, status=status.HTTP_201_CREATED)

    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   
    

class UpdateData(APIView):
    def get(self, request, pk):
        query = Persion.objects.get(pk=pk)
        serializers = PersionModelSerilizers(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Persion.objects.get(pk=pk)
        serializers = PersionModelSerilizers(query, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostData(APIView):
    def post(self, request):
        serializers = PersionModelSerilizers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchData(APIView):
    def get(self, request):
        search = request.GET['name']
        query = Persion.objects.filter(first_name__contains=search)
        serializers = PersionModelSerilizers(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    

class DeleteData(APIView):
    def get(self, request, pk):
        query = Persion.objects.get(pk=pk)
        serializers = PersionModelSerilizers(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Persion.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SearchDataDate(ListAPIView):
    # serializers = PersionModelSerilizers
    serializer_class = PersionModelSerilizers
    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        # start_date = self.request.parser_context.get('start_date')
        # end_date = self.request.parser_context.get('end_date')
        query = Persion.objects.filter(code_melli__range=(start_date, end_date))
        # serializers = PersionModelSerilizers(query)
        # return Response(serializers.data, status=status.HTTP_200_OK)
        return query


    # def get(self, request, **kwargs):
    #     start_date = kwargs.get('start_date')
    #     end_date = kwargs.get('end_date')
    #     # search = request.GET['range']
    #     # search_split = search.split(",")
    #     query = Persion.objects.filter(code_melli__range=(start_date, end_date))
    #     serializers = PersionModelSerilizers(query)

    #     return Response(serializers.data, status=status.HTTP_200_OK)


class FilterMultiFieldData(ListAPIView):
    queryset = Persion.objects.all()
    serializer_class = PersionModelSerilizers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']
    # queryset = Persion.objects.filter()


class SearchMultiFieldData(ListAPIView):
    queryset = Persion.objects.all()
    serializer_class = PersionModelSerilizers
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

