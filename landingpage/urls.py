# give every app default path
# one project path, one app path urls



from django.urls import path
from . import views

app_name = "landingpage"
urlpatterns = [
    path('', views.welcome, name = "welcome"),
    path('about', views.about, name = "about"),
    path('services', views.services, name = "services"),
    path('contact', views.contact, name = "contact")
]