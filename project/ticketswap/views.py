from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms
from django.forms import widgets

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm
from .models import Event, Listing, University, User, Message
from django.db.models import Q


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class EventCreate(CreateView):
    model = Event
    fields = ["name", "date", "location", "description", "universities", "cover"]
    def get_form(self):
        '''add date picker in forms'''
        form = super(EventCreate, self).get_form()

        form.fields['date'].widget = forms.SelectDateWidget()
        return form
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
    fields = ["event", "price", "quantity", "description"]
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.universiy = user
        return super().form_valid(form)

    # def get_form(self):
    #     '''add date picker in forms'''
    #     form = super(ListingCreate, self).get_form()
    #     form.fields['pub_date'].widget = forms.SelectDateWidget()
    #     return form
    success_url = "/ticketswap/"


class MessageCreate(CreateView):
    model = Message
    fields = ["receiver", "message"]
    def form_valid(self, form):
        sender = self.request.user
        form.instance.sender = sender
        return super().form_valid(form)
    success_url = "/ticketswap/profile"



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
        print(context)
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



class UserUpdate(UpdateView):
    model = User
    fields = ["username", "email", "university", "venmo"]
    success_url = "/ticketswap/"


class UserDelete(DeleteView):
    model = User
    success_url = "/ticketswap/accounts/login"


# def buyTicket(request, pk):
#     args = {"listing": Listing.objects.filter(listing=pk)}
#     return render(request, "buy_ticket.html", args)


def eventListings(request, pk):
    args = {"listings": Listing.objects.filter(event=pk)}  # TODO filter on event

    # args = {"listings": Listing.objects.filter(event ==pk)}  # TODO filter on event

    return render(request, "event_listings.html", args)

@login_required
def profile_page(request):
    args = {"listings" : Listing.objects.filter(user=request.user), "chats": Message.objects.all().order_by('pub_date').reverse()}
    return render(request, "profile_page.html", args)

@login_required
def index(request):
    # Event.objects.filter(universities=pk)
    # args = {"events": Event.objects.all()}  # TODO filter on uni
    args = {"events" : Event.objects.filter(universities=request.user.university)} 

    return render(request, "home.html", args)