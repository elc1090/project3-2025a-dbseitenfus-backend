from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/$', views.UsersList.as_view(), name='user-list'),
]