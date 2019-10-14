from . models import Bank
from rest_framework import serializers

class BankDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bank
		fields = '__all__'
