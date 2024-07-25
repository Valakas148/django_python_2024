from django.db.models import QuerySet
from django.http import QueryDict

from first.models import CarModel


def car_filter(query: QueryDict)-> QuerySet:
    qs = CarModel.objects.all()
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
            # case 'brand_start':
            #     qs = qs.filter(brand__in=[value].order_by(value))
    return qs