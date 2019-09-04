from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
import views

urlpatterns = (
	url(r'^login$',obtain_jwt_token),
	url(r'^getUsers$',views.getUsers),
	url(r'^signup$',views.signup),
	url(r'^register$',views.register),
	url(r'^forgotPassword$',views.forgotPassword),
	url(r'^changePassword$',views.changePassword),
)