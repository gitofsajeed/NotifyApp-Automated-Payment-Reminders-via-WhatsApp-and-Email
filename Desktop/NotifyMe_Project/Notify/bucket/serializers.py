from rest_framework import serializers
from .models import Loan, Insure, Rent


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"


class InsureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insure
        fields = ['title', 'type', 'initial_payment', 'noti_email', 'whatsapp_no', 'payment_intervel', 'schedule_time', 'schedule_day']

class rentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = ['title', 'type', 'initial_payment', 'noti_email', 'whatsapp_no', 'payment_period', 'schedule_time', 'schedule_day' ]