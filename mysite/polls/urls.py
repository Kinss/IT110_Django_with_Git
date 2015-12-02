from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', include(admin.site.urls)),
]

urlpatterns = [
	url(r'^$', views.index, name='index'),
]