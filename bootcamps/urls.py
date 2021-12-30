from django.urls import path
from . import views

urlpatterns = [
  path("/", views.getAllBootcamps),
  path("/<int:id>", views.getBootcampById),
  path("/", views.createBootcamp),
  path("/<int:id>", views.updateBootcamp),
  path("/<int:id>", views.deleteBootcamp)
]