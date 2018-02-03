
from django.conf.urls import url

from interface_login import views

app_name = 'interface_login'

urlpatterns = [
    # If the url is equal to "" then call views.LoginView.
    url(r'^$', views.LoginView.as_view(), name='login'),
]
