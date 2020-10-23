from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, University, Event, Listing, Transaction

admin.site.register(User, UserAdmin)
admin.site.register(University)
admin.site.register(Event)
admin.site.register(Listing)
admin.site.register(Transaction)
