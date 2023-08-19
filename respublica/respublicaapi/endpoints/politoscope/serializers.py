from rest_framework import serializers
from .models import Government, Senat, NationalAssembly, ConstitutionalCouncil, EuropeanParliament

class GovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Government
        fields = ('first_name', 'last_name', 'role', 'party', 'mandate_start', 'mandate_end', 'additional_mandate', 'picture', 'description', 'official_place')

class SenatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senat
        fields = ('first_name', 'last_name', 'role', 'party', 'mandate_start', 'mandate_end', 'additional_mandate', 'picture', 'description')

class NationalAssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalAssembly
        fields = ('first_name', 'last_name', 'role', 'party', 'mandate_start', 'mandate_end', 'additional_mandate', 'picture', 'description')

class ConstitutionalCouncilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstitutionalCouncil
        fields = ('first_name', 'last_name', 'role', 'mandate_start', 'mandate_end', 'nominator', 'picture', 'description')

class EuropeanParliamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EuropeanParliament
        fields = ('first_name', 'last_name', 'role', 'party', 'mandate_start', 'mandate_end', 'additional_mandate', 'picture', 'description')