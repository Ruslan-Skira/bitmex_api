from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Order
from api.serializers import OrderSerializer


class OrdersList(APIView):
    """
    List all Orders, or create a new order
    """
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, statu=status.HTTP_400_BAD_REQUEST)






class OrderDetail(APIView):
    """
    Retrieve, update or delete a code order.
    """
    def get_object(self, pk):
        try:
            return Order.object.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def dele(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    # try:
    #     order = Order.objects.get(pk=pk)
    # except Order.DoesNotExist:
    #     return HttpResponse(status=404)

    # if request.method == 'GET':
    #     serializer = OrderSerializer(order)
    #     return JsonResponse(serializer.data)
    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = OrderSerializer(order, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serilazer.errors, status=400)
    # elif request.method == 'DELETE':
    #     order.delete()
    #     return HttpResponse(status=204)
