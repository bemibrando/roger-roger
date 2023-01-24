from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('finance/', index),
    path('finance/update', update_finances),
    path('finance/update/qrcode', read_qr_code, name="read_qr_code"),
]