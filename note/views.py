from django.shortcuts import render
from .models import Note
# Create your views here.

def mapNote(request):

    if(request.method == 'POST'):
        note_heading = request.POST['note_heading']
        note = request.POST['note']
        lat = request.POST['lat']
        lng = request.POST['lng']

        fullnote = Note(note_heading=note_heading,note=note,lat=lat,lon=lng)
        fullnote.save()

        return render(request, 'index.html')


