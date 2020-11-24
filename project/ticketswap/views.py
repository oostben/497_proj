from django.shortcuts import get_object_or_404, render
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
        """add date picker in forms"""
        form = super(EventCreate, self).get_form()

        form.fields["date"].widget = forms.SelectDateWidget()
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

    def get_success_url(self):
        r_id = self.object.receiver.pk
        return f"/ticketswap/message/conv/{r_id}"


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
    args = {
        "listings": Listing.objects.filter(user=request.user),
        "chats": Message.objects.all().order_by("pub_date").reverse(),
    }
    return render(request, "profile_page.html", args)


@login_required
def index(request):
    args = {"events": Event.objects.filter(universities=request.user.university)}

    return render(request, "home.html", args)


@login_required
def message(request):
    messages = Message.for_user(request.user)
    other_users = set()
    for m in messages:
        if m.sender == request.user:
            other_users.add(m.receiver)
        else:
            other_users.add(m.sender)

    class Conversation:
        def __init__(self, messages):
            self.messages = messages
            self.len = len(messages)
            sorted(self.messages, key=lambda x: x.pub_date)

    conversations = {}
    for user in other_users:
        conversations[user] = Conversation(
            [m for m in messages if (m.sender == user or m.receiver == user)]
        )

    args = {"conversations": conversations}

    return render(request, "message.html", args)


@login_required
def message_user(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.for_user(request.user)

    messages = [
        m for m in messages if (m.sender == other_user or m.receiver == other_user)
    ]

    sorted(messages, key=lambda x: x.pub_date)

    # 'x_' needed to avoid name collision with session messages
    args = {"other_user": other_user, "x_messages": messages}

    return render(request, "message_user.html", args)
