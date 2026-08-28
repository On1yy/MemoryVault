from .models import Memory
from django import forms

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['title','text']
        labels = {
            'title':'',
            'text':'',
        }
        widgets = {

            "title": forms.TextInput(attrs={

                "placeholder": "Как бы вы его назвали?"

            }),

            "text": forms.Textarea(attrs={

                "placeholder": "Опишите здесь свое воспоминание..."

            })
        }



