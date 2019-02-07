from django import forms

class BoardForm(forms.Form):

    title = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : '제목',
                'required' : True,
            }
        )
    )

    author = forms.CharField(
        widget = forms.HiddenInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : '작성자',
                'readonly' : True,
            }
        )
    )

    context = forms.CharField(
        widget = forms.TextInput(
            attrs= {
                'class' : 'form-control',
                'placeholder' : '내용',
                'required' : True,
            }
        )
    )