from .models import Loan, Offer
from rest_framework import serializers


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
class OfferSerializer(serializers.ModelSerializer):
    loans = LoanSerializer(many=True,read_only=True)
    class Meta:
        model = Offer
        fields = '__all__'

class AOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('agree',)

class CompleteLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('completed',)



