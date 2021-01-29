from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView
from rest_framework import generics, status 
from rest_framework.response import Response
from .models import Loan, Offer, Investor
from .serializers import LoanSerializer, OfferSerializer, AOfferSerializer,\
                                        CompleteLoanSerializer
from . utils import funded, check_funded
                            
# Create your views here.

check_funded()
class LoansList(generics.ListCreateAPIView ):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
 
class LoanDetails(generics.RetrieveUpdateDestroyAPIView ):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer 
    lookup_field = 'id'

class LoanOffers(APIView):
    def get(self,request,loan_id):
        loan = get_object_or_404(Loan,pk=loan_id)
        offers = loan.offers.order_by('-created')
        data = OfferSerializer(offers,many=True).data
        return Response(data)
    def post(self,request,loan_id):
        data = request.data
        data['loan'] = loan_id
        data['investor'] = request.user.id
        data['first_name'] = request.user.investor.first_name
        data['last_name'] = request.user.investor.last_name
        data['email'] = request.user.investor.email
        serializer = OfferSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AcceptOffer(APIView):
    def get(self,request,loan_id,offer_id):
        offer = get_object_or_404(Offer,pk=offer_id)
        data = OfferSerializer(offer).data
        return Response(data)
    def put(self,request,loan_id,offer_id):
        data = JSONParser().parse(request)
        loan = Loan.objects.get(pk=loan_id)
        offer = Offer.objects.get(pk=offer_id)
        inv_id = int(offer.investor.id)
        investor = Investor.objects.get(pk=inv_id)
        serializer = AOfferSerializer(offer,data= data)
        if serializer.is_valid():
            serializer.save() 
            funded(loan,investor)
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CompleteLoan(APIView):
    def get(self,request,loan_id,inv_id):
        loan = get_object_or_404(Loan,pk=loan_id)
        data = LoanSerializer(loan).data
        return Response(data)
    def put(self,request,loan_id,inv_id):
        data = JSONParser().parse(request)
        loan = Loan.objects.get(pk=loan_id)
        serializer = CompleteLoanSerializer(loan,data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)