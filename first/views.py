from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from first.models import CarModel
from first.serializer import CarSerializer
from rest_framework.generics import GenericAPIView

# Create your views here.

class CarView(GenericAPIView):

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CarViewUpdateDelte(GenericAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get(self, *args, **kwargs):

        car = self.get_object()
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):

        data = self.request.data
        car = self.get_object()
        serializer = CarSerializer(car, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, *args, **kwargs):
        data = self.request.data
        car = self.get_object()
        serializer = CarSerializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        self.get_object().delete()
        return Response('', status=status.HTTP_204_NO_CONTENT)