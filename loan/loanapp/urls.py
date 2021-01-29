from django.urls import path
from . import views 
app_name = 'loanapp'

urlpatterns = [
        path('loans/', views.LoansList.as_view(), name='loans_list'),
        path('loan/<int:id>/', views.LoanDetails.as_view(), name='loan_details'),
        path('loan/offers/<int:loan_id>/', views.LoanOffers.as_view(),\
                                                     name='offer'),
        path('accept_offer/<int:loan_id>/<int:offer_id>',\
                     views.AcceptOffer.as_view(), name='accept_offer'),
        path('loan/<int:loan_id>-<int:inv_id>/complete/',\
                 views.CompleteLoan.as_view(), name='complete_offer'),
        
             ]
