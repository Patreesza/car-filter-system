from django.db.models import Count
from django.test import TestCase, Client
from django.urls import reverse

from car_app.forms import CarSearchForm
from car_app.models import CarModel, COLOR_CHOICES
from car_app.service import CarListService


class CarSearchTests(TestCase):
    @classmethod
    def setUp(cls):
        colors = [c[0] for c in COLOR_CHOICES]
        for i in range(10):
            CarModel.objects.create(
                name=f"ABC{i}",
                length=1500 * i,
                width=3000 * i,
                weight=450 + i,
                velocity=28.67 * 0.5,
                color=colors[i],
            )
        cls.client = Client()
        cls.url = reverse("car-list")
        cls.initial_form = {
            "name": "",
            "length_min": None,
            "length_max": None,
            "width_min": None,
            "width_max": None,
            "weight_min": None,
            "weight_max": None,
            "velocity_min": None,
            "velocity_max": None,
            "color": "-",
        }

    def tearDown(self):
        pass

    def test_get_index(self):
        response = self.client.get(self.url)
        form = response.context_data["car_search_form"]

        self.assertEqual(len(form.fields), 10)
        self.assertIn("name", form.fields)
        self.assertIn("length_min", form.fields)
        self.assertIn("length_max", form.fields)
        self.assertIn("width_min", form.fields)
        self.assertIn("width_max", form.fields)
        self.assertIn("velocity_min", form.fields)
        self.assertIn("velocity_max", form.fields)
        self.assertIn("weight_min", form.fields)
        self.assertIn("weight_max", form.fields)
        self.assertIn("color", form.fields)
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, "cars.html")

    def test_post_search_form(self):
        self.initial_form["name"] = "ABC1"
        response = self.client.post(
            self.url, {"car_search_form": CarSearchForm(self.initial_form)}
        )

        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, "cars.html")
        self.assertContains(response, "ABC1")

    def test_post_search_form2(self):
        self.initial_form["length_max"] = 1500
        response = self.client.post(
            self.url, {"car_search_form": CarSearchForm(self.initial_form)}
        )

        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, "cars.html")
        self.assertContains(response, "ABC1")

    def test_post_export(self):
        response = self.client.post(
            self.url,
            {
                "export": "EXPORT RESULT",
                "car_search_form": CarSearchForm(self.initial_form),
            },
        )

        self.assertTrue(response.status_code, 200)

    def test_service_search_empty(self):
        self.initial_form["name"] = "XYZ"

        form = CarSearchForm(self.initial_form)
        form.is_valid()
        qs = CarListService.search(self, data=form.cleaned_data)
        assert len([q.name for q in qs]) == 0

    def test_service_search(self):
        self.initial_form["color"] = "BLACK"

        form = CarSearchForm(self.initial_form)
        form.is_valid()
        qs = CarListService.search(self, data=form.cleaned_data)
        assert len([q.name for q in qs]) == 1
