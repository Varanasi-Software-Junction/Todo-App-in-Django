from django import forms
from django.forms import ModelForm, TextInput, DateTimeField

from .models import TodoModel


class TodoForm(ModelForm):
    class Meta:
        model = TodoModel
        # fields = fields = '__all__'
        fields = ['task', 'description', 'status','dateoftask']
        widgets = {
            'task': TextInput(attrs={
                'class': "form-control",
                'id':'taskinput',
                'placeholder': 'Task','required':''
            }
            )
            ,
            'description': TextInput(attrs={
                'class': "form-control",
                'id': 'descriptioninput',
                'placeholder': 'Task','required':''
            }
            )
            ,
            'status': TextInput(attrs={
                'class': "form-control",
                'id': 'descriptioninput',
                'placeholder': 'Status','required':''
            }
            )
            ,
            'dateoftask': TextInput(attrs={
                'class': "form-control",
                'id': 'dateinput',
                'placeholder': 'Date'
                ,
                'type':'date',
                'required':''
            }
            )




        }

"""

        <div class="form-floating mb-3">
  <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
  <label for="floatingInput">Email address</label>
</div>

"""