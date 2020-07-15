from django.contrib import admin

# Register your models here.
from sale.models import Offer, Advertisement

admin.site.register(Advertisement)
admin.site. register(Offer)
