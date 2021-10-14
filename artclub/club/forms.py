from django import forms


from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name',
                  'email',
                  'subject',
                  'message' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': '123@abc.xyz', 'required': 'required'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Subject', 'required': 'required'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Message....', 'required': 'required'})
        }
