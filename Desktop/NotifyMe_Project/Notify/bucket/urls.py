from django.urls import path
from bucket import views

urlpatterns = [
    path('loanlist/', views.LoanListCreate.as_view()),
    path('loandetail/<pk>/', views.LoanDetail.as_view()),
    path('insurelist/',views.InsureListCreate.as_view()),
    path('insure/<pk>/',views.InsureDetail.as_view()),
     path('rentlist/',views.RentListCreate.as_view()),
    path('rent/<pk>/',views.RentDetail.as_view()),

]
     