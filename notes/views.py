from django.shortcuts import render
from .models import Note
from .forms import CreateNote

def index(request): 
    notes = Note.objects.all().order_by("date")
    form = CreateNote(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    context = {"notes": notes, "form": form}
    return render(request, 'notes/index.html', context)

