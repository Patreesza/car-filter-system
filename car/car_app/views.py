import logging

from typing import Any
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView

from car_app.forms import CarSearchForm
from car_app.models import CarModel
from car_app.service import CarListService


logger = logging.getLogger(__name__)


class CarListView(ListView):
    """
    Contains list of cars.
    Can search a car.
    """

    model = CarModel
    template_name = "cars.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({"car_search_form": CarSearchForm()})
        return context

    def post(self, request, *args, **kwargs):
        is_search = True
        form = CarSearchForm(request.POST)

        if "export" in request.POST:
            is_search = False

        if form.is_valid():
            car_service = CarListService()
            self.object_list = car_service.search(form.cleaned_data)
            if self.object_list.count() == 0:
                messages.warning(self.request, "Empty list.")

            if not is_search:
                XMLSerializer = serializers.get_serializer("xml")
                xml_serializer = XMLSerializer()
                data = xml_serializer.serialize(self.object_list)
                return HttpResponse(
                    data,
                    content_type="application/xml",
                    headers={
                        "Content-Disposition": 'attachment; filename="car_list.xml"'
                    },
                )
        else:
            self.object_list = self.get_queryset()
            logger.warning(
                "Invalid form from car search."
            )  # It raise form error in page and at the same time, logs warning
        context = self.get_context_data(**kwargs)
        context.update({"car_search_form": form})
        return self.render_to_response(context, *args, **kwargs)
