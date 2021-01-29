from django.contrib import admin
from . models import Loan, Offer, Investor
# Register your models here.
admin.site.register(Loan)
admin.site.register(Offer)
admin.site.register(Investor)
