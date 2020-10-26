from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm
from .models import Event, University


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class EventCreate(CreateView):
    model = Event
    fields = ["name", "time", "location", "description", "universities"]
    success_url = "/ticketswap/"


class EventUpdate(UpdateView):
    model = Event
    fields = ["name", "time", "location", "description", "universities"]
    success_url = "/ticketswap/"


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy("/ticketswap/")


# ///////////////////////////////////////////


class UniversityCreate(CreateView):
    model = University
    fields = ["name"]
    success_url = "/ticketswap/"


class UniversityUpdate(UpdateView):
    model = University
    fields = ["name"]
    success_url = "/ticketswap/"


class UniversityDelete(DeleteView):
    model = University
    success_url = reverse_lazy("/ticketswap/")


@login_required
def index(request):
    args = {"events": Event.objects.all()}  # TODO filter on uno

    return render(request, "home.html", args)
