from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Investor(models.Model):
    user = models.OneToOneField(User,verbose_name="user",on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=200)
    balance = models.DecimalField(max_digits=7, decimal_places=2,default = 0)
    def __str__(self):
        return str(self.id)
class Loan(models.Model):
    borrower = models.ForeignKey(User,verbose_name="user",\
                                    on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE,null = True,blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    period = models.DecimalField(max_digits=3, decimal_places=1) 
    description = models.TextField(max_length=400) 
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    finish_date = models.DateTimeField(null = True ,blank = True)
    completed = models.BooleanField(default=False)
    funded = models.BooleanField(default=False)
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return str(self.id)
    
class Offer(models.Model):
    loan = models.ForeignKey(Loan,on_delete=models.CASCADE,\
                             related_name='offers')
    investor = models.ForeignKey(Investor,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    annual_interest_rate = models.DecimalField(max_digits=2, decimal_places=0, ) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    agree = models.BooleanField(default=False)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Offered by {self.first_name} {self.last_name} on {self.loan}'
