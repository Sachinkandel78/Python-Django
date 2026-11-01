from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
# Create your views here.

def home(request):
    print("someone made request on home page")
    courses = Course.objects.all()
    user_authenticated = False

    return render(request, "core/home.html",{
        "courses": courses,
        "user_authenticated": user_authenticated
    })


def courses(request):
    print("Someone made request in courses page")






    # return HttpResponse("Hello, I am Sachin! My Django Project is Running")
    # # return render(request,"code.html")
