from django.shortcuts import render
from .models import Geoshp
from note.models import Note
# Create your views here.
def Index(request):
    shp = Geoshp.objects.all()
    note = Note.objects.all()
    return render(request,'index.html',{'shp':shp,'note':note})
