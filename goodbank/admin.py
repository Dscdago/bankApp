from django.contrib import admin

from .models import User, UserProfile, Accounts, CreditApp, CreditAccounts, Transactions

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Accounts)
admin.site.register(CreditApp)
admin.site.register(CreditAccounts)
admin.site.register(Transactions)