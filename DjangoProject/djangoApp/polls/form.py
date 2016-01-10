from django import forms
from models import Person


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


class Meta:
    model = Person
    fields = ('name', 'email')


def save(self, commit=True):
    person = super(RegistrationForm, self).save(commit=False)
    person.email = self.cleaned_data['email']
    person.name = self.cleaned_data['name']
    if commit:
        person.save()

    return person
