from typing import Any

from car_app.models import CarModel
from django.db.models import QuerySet
from django.db.models import Q


class CarListService:
    def search(self, data: dict[str, Any]) -> QuerySet:
        # Length
        qlmn = Q()
        if data["length_min"]:
            qlmn = Q(length__gte=data["length_min"])
        qlmx = Q()
        if data["length_max"]:
            qlmx = Q(length__lte=data["length_max"])
        # Width
        qwmn = Q()
        if data["width_min"]:
            qwmn = Q(width__gte=data["width_min"])
        qwmx = Q()
        if data["width_max"]:
            qwmx = Q(width__lte=data["width_max"])
        # Velocity
        qvmn = Q()
        if data["velocity_min"]:
            qvmn = Q(velocity__gte=data["velocity_min"])
        qvmx = Q()
        if data["velocity_max"]:
            qvmx = Q(velocity__lte=data["velocity_max"])
        # Weight
        qwgmn = Q()
        if data["weight_min"]:
            qwgmn = Q(weight__gte=data["weight_min"])
        qwgmx = Q()
        if data["weight_max"]:
            qwgmx = Q(weight__lte=data["weight_max"])
        q = (
            Q(name__icontains=data.get("name", ""))
            & Q(color__icontains=data.get("color", ""))
        ) | (Q(qlmn & qlmx) & Q(qwmn & qwmx) & Q(qvmn & qvmx) & Q(qwgmn & qwgmx))

        qs = CarModel.objects.filter(q)
        return qs
