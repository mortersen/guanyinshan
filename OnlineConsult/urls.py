from django.urls import path
from .views import *


app_name = 'OnlineConsult'


urlpatterns = [
    path('',consult_main,name='consult_main'),
]