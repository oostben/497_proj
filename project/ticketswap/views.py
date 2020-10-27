from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm
from .models import Event, Listing, University


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


class ListingCreate(CreateView):
    model = Listing
    fields = ["user", "event", "pub_date", "price", "quantity", "description"]
    success_url = "/ticketswap/"


class ListingUpdate(UpdateView):
    model = Listing
    fields = ["user", "event", "pub_date", "price", "quantity", "description"]
    success_url = "/ticketswap/"


class ListingDelete(DeleteView):
    model = Listing
    success_url = reverse_lazy("/ticketswap/")


class ListingDetail(DetailView):
    model = Listing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


def eventListings(request, pk):
    pk = 1 # TOD0: pk = the event.id we are going to
    args = {"listings": Listing.objects.all()}  # TODO filter on event

    return render(request, "event_listings.html", args)


@login_required
def index(request):
    args = {"events": Event.objects.all()}  # TODO filter on uni

    return render(request, "home.html", args)