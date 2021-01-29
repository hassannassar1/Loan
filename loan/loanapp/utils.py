from dateutil.relativedelta import relativedelta
from datetime import datetime
from .models import Loan, Offer, Investor
FEES = 3
def funded(loan,investor):
    try:
        money = loan.amount+FEES
        if money <= investor.balance:
            loan.funded = True
            investor.balance = investor.balance - money
            months = int(loan.period)%12
            years = int(loan.period)//12
            loan.finish_date = datetime.now()+relativedelta(years=years,months=months)
            loan.save()
            investor.save()
    except:
        return
def check_funded():
    try:
        offers = Offer.objects.all()
        for offer in offers:
            if offer.agree == True:
                loan = Loan.objects.get(pk=offer.loan.id)
                if loan.funded==False:
                    inv = Investor.objects.get(pk=offer.investor.id)
                    funded(loan,inv)
    except:
        return