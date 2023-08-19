from rest_framework import viewsets

from .serializers import GovernmentSerializer, SenatSerializer, NationalAssemblySerializer, ConstitutionalCouncilSerializer, EuropeanParliamentSerializer
from .models import Government, Senat, NationalAssembly, ConstitutionalCouncil, EuropeanParliament


class GovernmentViewSet(viewsets.ModelViewSet):
    queryset = Government.objects.all()
    serializer_class = GovernmentSerializer

class SenatViewSet(viewsets.ModelViewSet):
    queryset = Senat.objects.all()
    serializer_class = SenatSerializer

class NationalAssemblyViewSet(viewsets.ModelViewSet):
    queryset = NationalAssembly.objects.all()
    serializer_class = NationalAssemblySerializer

class ConstitutionalCouncilViewSet(viewsets.ModelViewSet):
    queryset = ConstitutionalCouncil.objects.all()
    serializer_class = ConstitutionalCouncilSerializer

class EuropeanParliamentViewSet(viewsets.ModelViewSet):
    queryset = EuropeanParliament.objects.all()
    serializer_class = EuropeanParliamentSerializer