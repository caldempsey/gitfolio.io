"""
Responsible for providing functions used to communicate User model tasks with the Django messages framework.
"""
from django.contrib import messages
from django.contrib.auth.models import User


def username_present(request):
    """
    Identify if the username provided exists.
    :param username: The username passed.
    :return: Return whether the username exists in the user model.
    """
    if User.objects.filter(username=request.user.username).exists():
        return True
    # We need to send a message to the Django messages framework.
    messages.error(request,
                   'Sorry, there is a problem with your account. Please contact the website administrator.')
    return False
