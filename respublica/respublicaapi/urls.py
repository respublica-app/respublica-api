from django.urls import include, path

from rest_framework import routers
from .endpoints.tools.views import ToolsViewSet
from .endpoints.politoscope.views import GovernmentViewSet, SenatViewSet, NationalAssemblyViewSet, ConstitutionalCouncilViewSet, EuropeanParliamentViewSet


router = routers.DefaultRouter()
router.register(r'tools', ToolsViewSet)
router.register(r'politoscope/government', GovernmentViewSet)
router.register(r'politoscope/senat', SenatViewSet)
router.register(r'politoscope/nationalassembly', NationalAssemblyViewSet)
router.register(r'politoscope/constitutionalcouncil', ConstitutionalCouncilViewSet)
router.register(r'politoscope/europeanparliament', EuropeanParliamentViewSet)

urlpatterns = [
   path('', include(router.urls))
]