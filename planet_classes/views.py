from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PlanetClass
from .serializers import PlanetClassSerializer


class PlanetClassListCreate(APIView):
	def get(self, request):
		roles = PlanetClass.objects.all()
		serializer = PlanetClassSerializer(roles, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = PlanetClassSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(
			data=serializer.errors,
			status=status.HTTP_400_BAD_REQUEST
		)