from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path("courses/", views.courses, name="courses"),
    path("courses/<course_id>/", course_detail)
    # path("contact/", views.contact, name="contact"),
]