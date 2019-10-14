from django.db import models
from django.db.models import Q

class Bank(models.Model):
	ifsc = models.CharField(max_length=11, primary_key=True)
	bank_id = models.IntegerField()
	bank_name = models.CharField(max_length=50)
	branch = models.CharField(max_length=80)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=50)

	def __str__(self):
		return self.ifsc + '-' + self.bank_name


	@staticmethod
	def get_branches_name(branch_substring):
		try:
			bank_list = Bank.objects.filter(branch__icontains=branch_substring)\
									.order_by('ifsc')
		except Exception as e:
			bank_list = None

		return bank_list

	@staticmethod
	def get_branch_match(search_text):
		try:
			bank_list = Bank.objects.filter(Q(ifsc__icontains=search_text) |
											Q(bank_id__icontains=search_text)|
											Q(bank_name__icontains=search_text)|
											Q(branch__icontains=search_text)|
											Q(address__icontains=search_text)|
											Q(city__icontains=search_text)|
											Q(district__icontains=search_text)|
											Q(state__icontains=search_text)
											).order_by('ifsc')
		except Exception as e:
			bank_list = None

		return bank_list




