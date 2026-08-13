from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountListCreateView(APIView):
	def get(self, request):
		accounts = Account.objects.all()
		serializer = AccountSerializer(accounts, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = AccountSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(
				serializer.data,
				status=status.HTTP_201_CREATED)
		return Response(
			serializer.errors,
			status=status.HTTP_400_BAD_REQUEST)


class AccountDetails(APIView):
	def get(self, request, pk):
		try:
			account = Account.objects.get(pk=pk)
		except Account.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if account is None:
			return Response(
				{'message': 'Account not found.'},
				status=status.HTTP_404_NOT_FOUND
			)

		serializer = AccountSerializer(account)
		return Response(serializer.data)