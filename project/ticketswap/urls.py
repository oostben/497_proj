from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
    path("event/create/", views.EventCreate.as_view(), name="event_create"),
    path("event/<pk>/update/", views.EventUpdate.as_view(), name="event_update"),
    path("event/<pk>/delete/", views.EventCreate.as_view(), name="event_delete"),
    path("listing/create/", views.ListingCreate.as_view(), name="listing_create"),
    path(
        "listing/<pk>/detail/",
        views.ListingDetail.as_view(template_name="listing_detail.html"),
        name="listing_detail",
    ),
    path("listing/<pk>/update/", views.ListingUpdate.as_view(), name="listing_update"),
    path("listing/<pk>/delete/", views.ListingCreate.as_view(), name="listing_delete"),
]
