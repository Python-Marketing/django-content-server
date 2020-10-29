# forms.py
from django import forms
from django_select2 import forms as s2forms
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget

from .models import BeautifulGumtreeQuery, GumtreeCategory, GumtreeLocation, GumtreeProvince, GumtreeCategoryLabel


class QueryForm(forms.ModelForm):

    province = forms.ModelChoiceField(
        queryset=GumtreeProvince.objects.all(),
        empty_label='South Africa',
        required=False
    )

    label = forms.ModelChoiceField(
        queryset=GumtreeCategoryLabel.objects.all(),
        empty_label='All Categories',
        label=u"Category Label",
        required=False
    )

    category = forms.ModelMultipleChoiceField(
        queryset=GumtreeCategory.objects.all(),
        label=u"Category",
        widget=ModelSelect2MultipleWidget(
            model=GumtreeCategory,
            search_fields=['name__icontains'],
            dependent_fields={'label': 'label'},
            max_results=500,
        )
    )
    location = forms.ModelMultipleChoiceField(
        queryset=GumtreeLocation.objects.all(),
        label=u"Location",
        widget=ModelSelect2MultipleWidget(
            model=GumtreeLocation,
            search_fields=['name__icontains'],
            dependent_fields={'province': 'province'},
            max_results=500,
        )
    )

    class Meta:
        ordering = ['-id']
        model = BeautifulGumtreeQuery
        fields = ['label', 'category', 'province', 'location', 'term', 'price_start', 'price_end']
        # widgets = {
        #     "category": CategoryWidget,
        #     "province": GumtreeProvinceWidget,
        # }
        #
