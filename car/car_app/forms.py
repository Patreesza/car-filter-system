from typing import Any
from django import forms

from car_app.models import COLOR_CHOICES


class CarSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
    )
    length_min = forms.IntegerField(
        required=False,
        label="Length (mm)",
        widget=forms.TextInput(attrs={"placeholder": "1300"}),
    )
    length_max = forms.IntegerField(
        required=False,
        label="Max Length (mm)",
        widget=forms.TextInput(attrs={"placeholder": "1300"}),
    )
    width_min = forms.IntegerField(
        required=False,
        label="Width (mm)",
        widget=forms.TextInput(attrs={"placeholder": "1000"}),
    )
    width_max = forms.IntegerField(
        required=False,
        label="Max Width (mm)",
        widget=forms.TextInput(attrs={"placeholder": "1000"}),
    )
    velocity_min = forms.IntegerField(
        required=False,
        label="Velocity (m/s)",
        widget=forms.TextInput(attrs={"placeholder": "20"}),
    )
    velocity_max = forms.IntegerField(
        required=False,
        label="Max Velocity (m/s)",
        widget=forms.TextInput(attrs={"placeholder": "20"}),
    )
    weight_min = forms.IntegerField(
        required=False,
        label="Weight (kg)",
        widget=forms.TextInput(attrs={"placeholder": "450"}),
    )
    weight_max = forms.IntegerField(
        required=False,
        label="Max Weight (kg)",
        widget=forms.TextInput(attrs={"placeholder": "450"}),
    )
    color = forms.ChoiceField(choices=COLOR_CHOICES, initial="")
