from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note

def home(request):
  if request.user.is_authenticated:
    return redirect("notes")
  
  return render(request,"notes/home.html")

@login_required
def notes(request):
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

    return redirect("notes")

  return render(request,"notes/create_note.html")


@login_required
def edit_note(request,id):
  note = get_object_or_404(
    Note,
    id=id,
    user=request.user
  )

  if request.method == "POST":
    note.title = request.POST["title"]
    note.content = request.POST["content"]

    note.save()

    return redirect("notes")

  return render(
    request,
    "notes/edit_note.html",
    {"note":note}
  )

@login_required
def delete_note(request,id):

  note = get_object_or_404(
    Note,
    id=id,
    user=request.user
  )

  if request.method == "POST":
    note.delete()
    return redirect("notes")

  return render(
    request,
    "notes/delete_note.html",
    {"note":note}
  )
