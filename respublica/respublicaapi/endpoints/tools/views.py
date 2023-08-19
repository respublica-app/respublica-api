from rest_framework import viewsets

from .serializers import ToolsSerializer
from .models import Tools


class ToolsViewSet(viewsets.ModelViewSet):
   queryset = Tools.objects.all()
   serializer_class = ToolsSerializer