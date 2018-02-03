from django.conf.urls import url
from django.urls import include

from interface_authenticate import views

app_name = 'interface_authenticate'

urlpatterns = [
    # If the url is equal to "" then call views.LoginView.
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
    url(r'^dashboard$', views.Dashboard.as_view(), name='dashboard'),
    # You must include this in your urls.py url(r'^oauth/', include('social_django.urls', namespace='social')),
]
#TODO Investigate why namespacing does not work in apps but works at project level
