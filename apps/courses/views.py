from django.shortcuts import render, redirect
from .models import Course

def index(request):
    content = {
        'courses': Course.objects.all()
    }
    
    return render(request, "courses/index.html", content)

def destroy(request, id):
    
    content = {
        'courses': Course.objects.get(pk=id)
    }
    
    return render(request, "courses/destroy.html", content)

def confirm(request, id):
    if request.method == "POST":
        
        Course.objects.get(pk=id).delete()
        return redirect('/')
    

def addCourse(request):
    if request.method == "POST":
        course = Course.objects.create(name=request.POST['courseName'],desc=request.POST['desc'])
        
        print course
        return redirect('/')
    return redirect('/')
