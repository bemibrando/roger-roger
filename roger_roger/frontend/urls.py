from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('finance/', index),
    path('finance/update', read_qr_code),
]