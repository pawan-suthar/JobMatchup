from django.conf import settings
from django.contrib import messages
#require to access pvt pages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
# used to redirect pages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from.models import *
# destroy the section after logout session
from django.views.decorators.cache import cache_control

# Create your views here.

# home page function
def home(request):
    return render(request, "home.html")

# job page function
def job_category(request):
    return render(request, "jobcategory.html")

#==================frontend=======================#
# email wale functions
def front_mail(request):
    if request.method == "POST":
        # check if email already exists
        email = request.POST.get('email')
        if Reg_email.objects.filter(email=email).exists():
            messages.error(request, "It looks like your resume has already been safely stored in our system.")
            return HttpResponseRedirect('/job_category')
        else:   
            name = request.POST.get('fullname')
            email = request.POST.get('email')
            age = request.POST.get('age')
            contactnumber = request.POST.get('contactnumber')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')
            # if email not save then saved here 

            contact = Reg_email()
            contact.email = email
            contact.save()

            # mail body me attach hoga ye txt
            template = loader.get_template('form.txt') 

            data = {
                'name':name,
                'email':email,
                'age':age,
                'contactnumber':contactnumber,
                'experience':experience,
                'skills':skills,
            }

            message = template.render(data)
            email = EmailMultiAlternatives(
                "frontend-person",message, #email ali tag line
                "frontend profile",
                ['receiver mail']
            )

            email.content_subtype = 'html'
            file = request.FILES['resume']
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request,f" dear {data.get('name')} your resume for frontend received ")
            return HttpResponseRedirect('/')


def back_mail(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if Reg_email.objects.filter(email=email).exists():
            messages.error(request, "It looks like your resume has already been safely stored in our system.")
            return HttpResponseRedirect('/job_category')
        else:
            name = request.POST.get('fullname')
            email = request.POST.get('email')
            age = request.POST.get('age')
            contactnumber = request.POST.get('contactnumber')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')

            # mail body me attach hoga ye txt
            template = loader.get_template('form.txt') 

            data = {
                'name':name,
                'email':email,
                'age':age,
                'contactnumber':contactnumber,
                'experience':experience,
                'skills':skills,
            }

            contact = Reg_email()
            contact.email = email
            contact.save()

            message = template.render(data)
            email = EmailMultiAlternatives(
                "backend-person",message, #email ali tag line
                "backend profile",
                ['receiver mail ']
            )

            email.content_subtype = 'html'
            file = request.FILES['resume']
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request,f" dear {data.get('name')} your resume for backend received ")
            email.send()
            return HttpResponseRedirect('/')    


def full_mail(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if Reg_email.objects.filter(email=email).exists():
            messages.error(request, "It looks like your resume has already been safely stored in our system.")
            return HttpResponseRedirect('/job_category')
        else:
            name = request.POST.get('fullname')
            email = request.POST.get('email')
            age = request.POST.get('age')
            contactnumber = request.POST.get('contactnumber')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')

            # mail body me attach hoga ye txt
            template = loader.get_template('form.txt') 

            data = {
                'name':name,
                'email':email,
                'age':age,
                'contactnumber':contactnumber,
                'experience':experience,
                'skills':skills,
            }

            contact = Reg_email()
            contact.email = email
            contact.save()

            message = template.render(data)
            email = EmailMultiAlternatives(
                "fullstack-person",message, #email ali tag line
                "fullstack profile",
                ['receiver mail']
            )

            email.content_subtype = 'html'
            file = request.FILES['resume']
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request,f" dear {data.get('name')} your resume for fullstack received ")
            return HttpResponseRedirect('/')  



def intern_mail(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if Reg_email.objects.filter(email=email).exists():
            messages.error(request, "It looks like your resume has already been safely stored in our system.")
            return HttpResponseRedirect('/job_category')
        else:
            name = request.POST.get('fullname')
            email = request.POST.get('email')
            age = request.POST.get('age')
            contactnumber = request.POST.get('contactnumber')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')

            # mail body me attach hoga ye txt
            template = loader.get_template('form.txt') 

            data = {
                'name':name,
                'email':email,
                'age':age,
                'contactnumber':contactnumber,
                'experience':experience,
                'skills':skills,
            }

            contact = Reg_email()
            contact.email = email
            contact.save()

            message = template.render(data)
            email = EmailMultiAlternatives(
                "intern-person",message, #email ali tag line
                "intern profile",
                ['receiver mail@gmail.com']
            )

            email.content_subtype = 'html'
            file = request.FILES['resume']
            email.attach(file.name,file.read(),file.content_type)
            email.send()
            messages.success(request,f" dear {data.get('name')} your resume for internship received ")
            return HttpResponseRedirect('/')  

#==================backend=======================#
@cache_control(no_cache = True, must_revalidate=True,no_store= True)
@login_required(login_url="login")
def backend(request):
    return render(request, 'registration/login.html')
