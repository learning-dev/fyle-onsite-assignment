from . serializers import BankDataSerializer
from . models import Bank
from . helpers import bankPagination

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
def get_branches_autocomplete(request):
	paginator = bankPagination()
	branch_substring = request.GET.get('q')
	branches = Bank.get_branches_name(branch_substring)
	if branches:
		page = paginator.paginate_queryset(branches, request)
		bank_serilizer = BankDataSerializer(page, many=True)
		return paginator.get_paginated_response(bank_serilizer.data)
	else:
		return Response({
			'message': 'Error: No such branch Found!'
			}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_branches(request):
	paginator = bankPagination()
	match_string = request.GET.get('q')

	branches = Bank.get_branch_match(match_string)
	if branches:
		page = paginator.paginate_queryset(branches, request)
		bank_serilizer = BankDataSerializer(page, many=True)
		return paginator.get_paginated_response(bank_serilizer.data)
	else:
		return Response({
			'message': 'Error: No such branch Found!'
			}, status=status.HTTP_404_NOT_FOUND)


