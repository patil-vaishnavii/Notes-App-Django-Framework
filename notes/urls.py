from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("notes/",views.notes,name="notes"),
 path("create/",views.create_note,name="create_note"),
 path("edit/<int:id>/",views.edit_note,name="edit_note"),
 path("delete/<int:id>/",views.delete_note,name="delete_note"),
]
