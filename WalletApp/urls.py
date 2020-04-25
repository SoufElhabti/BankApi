from django.contrib import admin
from django.urls import path, include
from wallet_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sentmoney/<str:id>/', views.MoneySent,name = 'MoneySent'),
    path('api/recievedmoney/<str:id>', views.MoneyReceived,name = 'MoneyReceived'),
    path('api/user/<str:key>', views.getUser,name = 'User'),
    path('api/transaction/' , views.MakeTansaction , name = 'transactionmaker'),
    path('api/login',views.login , name = 'loginpage')
]
