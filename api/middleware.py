# We can define Our Logics of Login a user here like different types and for different priorities,
# Here is the code that was required in the task

from django.shortcuts import render
from django.urls import reverse


class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the Request is relevent to the app or Admin panel
        if not request.path.startswith('/admin/'):
            if not request.user.is_authenticated:
                if request.method == 'POST' and request.path == reverse('login'):
                    return self.get_response(request)
                else:
                    return render(request, 'login.html')

        # For all other URLs (including admin URLs), proceed with normal processing
        return self.get_response(request)
