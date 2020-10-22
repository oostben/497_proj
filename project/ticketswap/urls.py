from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
