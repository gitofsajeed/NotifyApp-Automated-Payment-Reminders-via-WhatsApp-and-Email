from rest_framework.views import APIView,Response
from django.shortcuts import render
from bucket.models import Loan, Insure, Rent
from rest_framework import generics
from .serializers import LoanSerializer, InsureSerializer,rentSerializer

# Create your views here.
# class loanBucket(APIView):
#     def createLoan(self):
# class insureBucket(APIView):
#     pass
# class rentBucket(APIView):
#     pass

class LoanListCreate(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer



class InsureListCreate(generics.ListCreateAPIView):
    queryset = Insure.objects.all()
    serializer_class = InsureSerializer

class InsureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insure.objects.all()
    serializer_class = InsureSerializer




class RentListCreate(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = InsureSerializer

class RentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = rentSerializer
    # comment