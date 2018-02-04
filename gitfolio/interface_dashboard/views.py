from django.shortcuts import render

from django.views import View


# Create your views here.

class Dashboard(View):
    dashboard_template = "dashboard.html"
    """
    The Dashboard template is responsible for providing the resources for rendering the user dashboard provided a username.
    """

    def get(self, request, username):
        # Get user profile at username.
        # Check if user belongs to the request.
        # If not then render to username public profile.
        # TODO Enforce no duplicate usernames
        return render(request, self.dashboard_template)
