from django.db import models
from datetime import datetime
# Create your models here.



class User(models.Model):

	email  =  models.EmailField(max_length = 200 , unique = True)
	password = models.CharField(max_length = 200 ,null = True)
	name = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	RIB   =  models.CharField(max_length = 150)
	CardNb = models.CharField(max_length = 150)
	balance = models.IntegerField()

	def __str__(self):
		return self.email 


class Transaction(models.Model ):
	Date = models.DateField(auto_now=True)
	amount = models.IntegerField()
	SenderId= models.ForeignKey(User, on_delete = models.CASCADE, related_name="TransactionSender")
	RecieverId = models.ForeignKey(User, on_delete = models.CASCADE, related_name="TransactionReciever")

	
	def __str__(self):
		return self.Date.strftime('%m/%d/%Y')
