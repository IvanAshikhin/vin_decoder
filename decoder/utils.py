from django.db.models import Count, Max
from .models import Car, User


def vin_search_count_with_date():
    return Car.objects.annotate(
        total_vin_search_count=Count("requestlog"),
        distinct_user_count=Count("requestlog__user"),
        last_search_date=Max("requestlog__created_at"),
    )


def user_vin_search_count_with_date(user_id):
    queryset = User.objects.filter(id=user_id).annotate(
        total_vin_search_count=Count("requestlog"),
        distinct_car_count=Count("requestlog__car"),
        last_search_date=Max("requestlog__created_at"),
    )

    return queryset
