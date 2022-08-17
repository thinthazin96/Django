from django.urls import path
from . import views
 
urlpatterns = [
     path("", views.project_index, name="project_index"),   #hook up the root URL of our app to the project_index view.
     path("<int:pk>/", views.project_detail, name="project_detail"),
 ]