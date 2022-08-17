from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    #Perform a query (A query is simply a command that allows you to create, retrieve, update, or delete objects (or rows) in your databases)
    projects = Project.objects.all() #retrive all the objects in the in the project table
    
    #context dic used to send information to template
    context = {                       
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_delete(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_delete.html', context)