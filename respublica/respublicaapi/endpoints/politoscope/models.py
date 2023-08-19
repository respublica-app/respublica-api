from django.db import models

class Government(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    mandate_start = models.DateField()
    mandate_end = models.DateField(blank=True, null=True)
    additional_mandate = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    official_place = models.CharField(max_length=100)

class Senat(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    mandate_start = models.DateField()
    mandate_end = models.DateField(blank=True, null=True)
    additional_mandate = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

class NationalAssembly(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    mandate_start = models.DateField()
    mandate_end = models.DateField(blank=True, null=True)
    additional_mandate = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

class ConstitutionalCouncil(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    mandate_start = models.DateField()
    mandate_end = models.DateField(blank=True, null=True)
    nominator = models.CharField(max_length=100, blank=True, null=True)
    picture = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

class EuropeanParliament(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    mandate_start = models.DateField()
    mandate_end = models.DateField(blank=True, null=True)
    additional_mandate = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)