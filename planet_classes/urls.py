from django.urls import path

from .views import PlanetClassListCreate

urlpatterns = [
	path('planet-class/', PlanetClassListCreate.as_view())
]