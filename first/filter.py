from django.db.models import QuerySet
from django.http import QueryDict

from first.models import CarModel
from first.serializer import CarSerializer


def car_filter(query: QueryDict)-> QuerySet:
    qs = CarModel.objects.all()
    serializer = CarSerializer()
    print('aaa')
    for key, value in query.items():
        match key:
            case 'price_gt':
                qs = qs.filter(price__gt=value)
            case 'price_lt':
                qs = qs.filter(price__lt=value)
            case 'price_ge':
                qs = qs.filter(price__ge=value)
            case 'price_le':
                qs = qs.filter(price__lt=value)
            case 'year_gt':
                qs = qs.filter(year__gt=value)
            case 'year_lt':
                qs = qs.filter(year__lt=value)
            case 'year_ge':
                qs = qs.filter(year__ge=value)
            case 'year_le':
                qs = qs.filter(year__lt=value)
            case 'brand_in':
                qs = qs.filter(brand__in=[value])
            case 'brand_start':
                 qs = qs.filter(brand__istartswith=value)
            case 'brand_end':
                qs = qs.filter(brand__iendswith=value)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=value)
            case 'order':
                fields = serializer.get_fields().keys()
                fields = list(fields) + [f'-{field}' for field in fields]
                if value not in fields:
                    raise ValueError(f'Uncorrect input')
                qs = qs.order_by(value)
            case _:
                return (f"Uncorrect params {key}")
    return qs