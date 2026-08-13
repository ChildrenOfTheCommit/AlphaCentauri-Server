from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from roles.models import Roles
from roles.serializers import RoleSerializer


class RoleListCreate(APIView):
	def get(self, request):
		roles = Roles.objects.all()
		serializer = RoleSerializer(roles, many=True)
		return Response(serializer.data)

	def post(self, rvee):
		serializer = RoleSerializer(data=rvee.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(
			data={'message': 'Invalid :P'},
			status=status.HTTP_400_BAD_REQUEST
		)