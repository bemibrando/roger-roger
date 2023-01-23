from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from .src.components.camera import *

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

@gzip.gzip_page
def read_qr_code(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass

    return render(request, 'update_finances.html')