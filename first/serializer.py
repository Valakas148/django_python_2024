from rest_framework import serializers

from first.models import CarModel


class CarSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=255)
    model = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    year = serializers.IntegerField()

    def create(self, validated_data: dict):
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()
            return instance