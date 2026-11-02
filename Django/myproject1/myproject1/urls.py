from django.contrib import admin
from django.urls import path
from myapp.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    # path("contact/", contact),
    path("about/", about),
    # yo "about/" vanney path ma pugda about function call hunxa ani yo function le HttpResponse return garxa.
    path("courses/<course_id>/", course_detail, name="course_detail"),
    
    # name diyo vaney yesari lamo courses/<course_id>/ vanera lekheylo path yad garirahanu pareyna sidhai name wala path samjiye vayo tei use garda short and sweet hunxa 
    # yo chai hami uta templates vitra ko .html file vitra ko href ma use garxau.
    path("courses/", courses, name="courses"),
]
