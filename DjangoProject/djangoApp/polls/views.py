from form import RegistrationForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import Person


def list_users(request):
    users_list = Person.objects.all()
    context_dict = {'users': users_list}

    return render(request, '../templates/list.html', context_dict)


def index(request):
    return render(request, '../templates/home.html')


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            person = Person()
            person.name = form.cleaned_data['name']
            person.email = form.cleaned_data['email']
            person.save()
            return HttpResponseRedirect('../list/')
    else:
        form = RegistrationForm()

    return render(request, '../templates/register.html', {'form': form})
