from openAPIs.models import *
import serpy

class ViewUsersSerializer(serpy.Serializer):
	username=serpy.Field()