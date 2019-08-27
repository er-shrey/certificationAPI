from skillcall.models import *
import serpy

class ViewUsers(serpy.Serializer):
	username=serpy.Field()
	seq=serpy.Field()