from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User Model
class User(AbstractUser):
    pass

# User Profile. Extends User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.CharField(max_length=10)
    address = models.CharField(max_length = 800)
    phoneNumber = models.CharField(max_length=10)
    firstLogin = models.BooleanField(default=True)

    def __str__(self):
        return f"User Profile of {self.user}"

# Accounts Model
class Accounts(models.Model):
    accountNumber = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="account")

    def __str__(self):
        return f"Account #{self.accountNumber} by {self.user.username} with ${self.balance}"

# Credit Application Model
class CreditApp(models.Model):
    status = models.CharField(max_length=6)
    approvedLimit = models.DecimalField(decimal_places=2)
    creditScore = models.IntegerField()
    estimatedDebt = models.DecimalField(decimal_places=2)
    yearlyIncome = models.DecimalField(decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Credit App for {self.user.username}. Status: {self.status}"

# Credit Account Model
class CreditAccounts(models.Model):
    accountNumber = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2)
    creditLimit = models.DecimalField(decimal_places=2)
    applicationID = models.ForeignKey(CreditApp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardNumber = models.CharField(max_length=200)

    def __str__(self):
        return f"Credit Acc #{self.accountNumber} for user: {self.user.username}"

# Transactions Model
class Transactions(models.Model):
    amount = models.DecimalField(decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=800)
    transactionType = models.CharField(max_length=10)
    accountNumber = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    cardNumber = models.ForeignKey(CreditAccounts, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction #{self.id}. Type: {self.transactionType}"
