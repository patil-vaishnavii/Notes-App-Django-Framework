from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def home(request):
  notes = Note.objects.filter(user=request.user) # to make app user-specific.

  return render(
    request,
    "notes/index.html",
    {"notes":notes}
  )

@login_required
def create_note(request):

  if request.method == "POST":
    title = request.POST["title"]
    content = request.POST["content"]

    Note.objects.create(
      user=request.user,
      title=title,
      content=content
    )

    return redirect("home")

  return render(request,"notes/create_note.html")
