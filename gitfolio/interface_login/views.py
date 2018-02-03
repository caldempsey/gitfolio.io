from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import View

#TODO Build such that if user is not logged in then instance login view class


class LoginView(View):
    """
    LoginView is responsible for facilitating the task of providing a login interface.
    """

    login_template = 'login.html'

    def get(self, request):
        return render(request, self.login_template)

    def post(self, request):
        """
        Handles login template details from users.
        """
        return redirect(request, self.login_template)
