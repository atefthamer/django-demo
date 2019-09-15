from django.urls import path
# from americanworkplace.views import home
from . import views

app_name = 'americanworkplace'

urlpatterns = [
    #path(r'^$', home, name="home"),
    path('', views.home),
]
