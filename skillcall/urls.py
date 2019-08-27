from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
import views

urlpatterns = (
	url(r'^login$',obtain_jwt_token),
	url(r'^getUsers$',views.getUsers),
)