from openAPIs.models import *
import serpy

class getFewCoursesSerializer(serpy.Serializer):
	course_name=serpy.Field()
	course_details=serpy.Field()
	course_pic=serpy.Field()
	category_name=serpy.Field()