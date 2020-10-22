from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def index(request):
    return HttpResponse("Hello! Welcome to the index of ticketswap")
