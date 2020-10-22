from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('event/create/', views.EventCreate.as_view(), name='event_create'),
    path('event/<pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    path('event/<pk>/delete/', views.EventCreate.as_view(), name='event_delete'),

    path('university/create/', views.UniversityCreate.as_view(), name='event_create'),
    path('university/<pk>/update/', views.UniversityUpdate.as_view(), name='event_update'),
    path('university/<pk>/delete/', views.UniversityCreate.as_view(), name='event_delete'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
