"""
Responsible for providing functions used to communicate authentication tasks with the Django messages framework.
"""
from django.contrib import messages
from requests import auth
from django.contrib import auth


def logout(request):
    # Django shortcut to cleanly logout a user from a request.
    auth.logout(request)
    messages.success(request,
                     'You have been logged out.')
    return None


def logout_silent(request):
    # Django shortcut to cleanly logout a user from a request.
    auth.logout(request)

    return None
