from django.urls import include, path

from rest_framework import routers
from respublicaapi.views import ToolsViewSet


router = routers.DefaultRouter()
router.register(r'tools', ToolsViewSet)

urlpatterns = [
   path('', include(router.urls)),
]