from django.shortcuts import render
from .models import Geoshp
# Create your views here.
def Index(request):
    shp = Geoshp.objects.all()
    return render(request,'index.html',{'shp':shp})
