"""
from django import forms

class BasketForm(forms.Form):

    name = forms.CharField(
        widget = forms.CharField(
            attrs = {
                'class' : 'form-control',
                'placeholder' : '메뉴이름',
                'readonly' : True,
            }
        )
    )

    price = forms.CharField(
        widget = forms.CharField(
            attrs = {
                'class' : 'form-control',
                'placeholder' : '가격',
                'readonly' : True,
            }
        )
    )

    count = forms.IntegerField(
        widget = forms.IntegerField(
            attrs= {
                'class' : 'form-control',
                'placeholder' : '수량',
                'required' : True,
            }
        )
    )
"""