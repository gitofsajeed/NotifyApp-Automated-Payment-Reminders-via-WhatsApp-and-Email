from django.db import models
from datetime import datetime
# from django.http import request

# Create your models here.


TYPE = [("Other","Other"), ("Car", "Car"), ("Mobile","Mobile"), ("Education","Education"), ("House","House"),("Health","Health") ]
PERIOD = [ ("Daily","Daily"), ("Weekly","Weekly"), ("Monthly","Monthly"), ("Yearly","Yearly") ]

def first_day_of_month():
        return datetime.today().replace(day=1)

class Loan(models.Model):
    title = models.CharField(max_length=20,default="Unknown",)
    type = models.CharField(choices = TYPE,max_length=20, default = "Other")
    total_amount = models.CharField(max_length=20, blank=False)
    initial_payment = models.CharField(max_length=20, blank=False)
    noti_email = models.EmailField(max_length=20,blank=True, default="example@gmail.com")#default= request.user.email)
    whatsapp_no = models.CharField(max_length=15,blank=False, ) #validators=[phone_number_validator]
    payment_period = models.CharField(choices = PERIOD, max_length=20, blank=False, default="Monthly")
    schedule_time = models.TimeField(blank=False, default=datetime.now())
    schedule_day = models.DateField(blank=False, default=first_day_of_month())

    # @classmethod
    # def get_by_id(cls, id):
    #     try:
    #         return cls.objects.get(id=id)
    #     except cls.DoesNotExist:
    #         raise ValueError("No loan with id {} found".format(id))

    # @classmethod
    # def remove_duplicates(cls):
    #     loans = cls.objects.all()
    #     unique_loans = set()
    #     for loan in loans:
    #         if loan.id not in unique_loans:
    #             unique_loans.add(loan.id)
    #     for loan in loans:
    #         if loan.id not in unique_loans:
    #             loan.delete()    


    def __str__(self):
        return self.title
    
class Insure(Loan):
    payment_intervel = models.CharField(choices = PERIOD, max_length=20, blank=False, default="Yearly")
    

class Rent(Insure):
    pass

    def __str__(self):
        return self.title



    
    

