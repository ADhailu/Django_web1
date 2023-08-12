from django.contrib import admin
from .models import Home, About, ContactPage, Contact
# Register your models here.
admin.site.register(Home)
admin.site.register(About)
admin.site.register(ContactPage)
admin.site.register(Contact)