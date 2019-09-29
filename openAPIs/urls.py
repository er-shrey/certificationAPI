from django.conf.urls import url
import views

urlpatterns = (
	url(r'^getCourses$',views.getCourses),
	url(r'^getPlatformInfo$',views.getPlatformInfo),
)