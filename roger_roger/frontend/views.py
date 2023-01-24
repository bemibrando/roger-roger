from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from .src.components.camera import *
from .src.components.finance.update_expenses import *

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

@gzip.gzip_page
def update_finances(request, *args, **kwargs):
    return render(request, 'frontend/update_finances.html')

def read_qr_code(request):    
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

    except:
        pass