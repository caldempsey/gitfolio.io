from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import View


# TODO Build such that if user is not logged in then instance login view class
# TODO Build index handler

class LoginView(View):
    """
    LoginView is responsible for facilitating the task of providing a login interface.
    """
    index_template = 'index.html'
    login_template = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.index_template)
        return render(request, self.login_template)

    def post(self, request):
        """
        Handles login template details from users.
        """
        return redirect(request, self.login_template)

class Dashboard(View):
    """
    LoginView is responsible for facilitating the task of providing a login interface.
    """
    index_template = 'index.html'

    def get(self, request):
        return render(request, self.index_template)


class LogoutView(View):
    """
    LogoutVIew is responsible for logging out users when called.
    """

    def get(self, request):
        # Django shortcut to cleanly logout a user from a request.
        auth.logout(request)
        return redirect('/')
