from rest_framework import serializers
from respublicaapi.models import Tools

class ToolsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tools
       fields = ('name', 'url', 'logo', 'category', 'official', 'author', 'description')