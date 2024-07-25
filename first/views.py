from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from first.filter import car_filter
from first.models import CarModel
from first.serializer import CarSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
# Create your views here.

class CarView(GenericAPIView, CreateModelMixin, ListModelMixin):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    def get(self, request ,*args, **kwargs):
        return super().list(request,*args, **kwargs)

    def post(self, request ,*args, **kwargs):
        return super().create(request,*args, **kwargs)

    def get_queryset(self):
        return car_filter(self.request.query_params)


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