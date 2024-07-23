from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from first.models import CarModel


# Create your views here.

class CarView(APIView):

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        res = [model_to_dict(car) for car in cars]
        return Response(res)

    def post(self, *args, **kwargs):
        data = self.request.data
        car = CarModel.objects.create(**data)
        car_dict = model_to_dict(car)
        return Response(car_dict)


class CarViewUpdateDelte(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)

        except CarModel.DoesNotExist:
            return Response('not found')

        return Response(model_to_dict(car))

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data

        try:
            car = CarModel.objects.get(pk=pk)

        except CarModel.DoesNotExist:
            return Response('not found')

        car.brand = data['brand']
        car.model = data['model']
        car.year = data['year']
        car.price = data['price']
        car.save()
        return Response(model_to_dict(car))

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk).delete()

        except CarModel.DoesNotExist:
            return Response('not found')

        return Response('')