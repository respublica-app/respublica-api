from rest_framework import viewsets

from respublicaapi.serializers import ToolsSerializer
from respublicaapi.models import Tools


class ToolsViewSet(viewsets.ModelViewSet):
   queryset = Tools.objects.all()
   serializer_class = ToolsSerializer