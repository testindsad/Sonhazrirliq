from django.conf import settings
from django.utils import timezone
from django.http import Http404
from django.middleware.csrf import CsrfViewMiddleware
from django.http import HttpResponseForbidden
from .models import BannedIP
from django.urls import resolve
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
class DisableCSRFMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request.path.startswith('/admin/'):
            return None
        return super().process_view(request, callback, callback_args, callback_kwargs)
class VisitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the session already contains a visit count
        visit_count = request.session.get('visit_count', 0)
        
        # Increment the visit count and update the session
        request.session['visit_count'] = visit_count + 1/20
        
        # Update the last visit timestamp
        request.session['last_visit'] = str(timezone.now())

        response = self.get_response(request)
        return response

class IPBanMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = request.META.get('REMOTE_ADDR')
        if BannedIP.objects.filter(ip_address=user_ip).exists():
            return HttpResponseForbidden("Your IP address is banned.")
        
        response = self.get_response(request)
        return response
    
