from django.conf.urls import url
from django.urls import include

from interface_dashboard import views

app_name = 'interface_dashboard'

# For the example in this implementation to work you must include this in your urls.py url(r'^oauth/',
# include('social_django.urls', namespace='social')), since this application is used in conjunction with the
# social_django packages. Otherwise feel free to ignore this.

urlpatterns = [
    # User dashboard view. Requires username.
    url(r'^(?P<username>([A-Za-z0-9]+(-[A-Za-z0-9]+)?)+$)', views.Dashboard.as_view(), name='dashboard'),
]
