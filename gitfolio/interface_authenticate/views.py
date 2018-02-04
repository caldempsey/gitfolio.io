from django.shortcuts import render, redirect
from django.views.generic import View

from interface_authenticate.communicate.auth import logout, logout_silent
from interface_authenticate.communicate.user import username_present


# TODO Build such that if user is not logged in then instance login view class
# TODO Build index handler

class LoginAuthHandler(View):
    """
    The AuthHandler class is responsible for determining whether users are sent to their profile page (are logged in)
    or the root page "/".
    """

    login_template = "login.html"
    def get(self, request):
        if request.user.is_authenticated:
            # Username present in the communicator package will communicate with the Django messages framework to
            # inform if there are issues with the account.
            if username_present(request):
                return redirect("/" + request.user.username)
            else:
                # Logout silent logs the user out but does not post to the Django messages framework (logs are still
                # recorded)
                logout_silent(request)
                return redirect("/")
        return render(request, self.login_template)

    def post(self, request):
        """
        Determined where the login request goes when the user logs in.
        """
        if request.user.is_authenticated:
            if username_present(request):
                return redirect("/" + request.user.username)
            else:
                logout_silent(request)
        return redirect("/")


class LogoutAuthHandler(View):
    """
    The AuthHandler class is responsible for determining whether users are sent to their profile page (are logged in)
    or the root page "/".
    """

    def get(self, request):
        if request.user.is_authenticated:
            if username_present(request):
                logout(request)
                return redirect("/" + request.user.username)
            else:
                logout_silent(request)
            return redirect("/")
        return redirect("/")

