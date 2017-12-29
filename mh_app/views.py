from django.shortcuts import render

# Create your views here.

def index(request):

        return render(request,"mh_app/index.html")

def blog(request):

        return render(request,"mh_app/blog.html")

def dashboard(request):

        return render(request,"mh_app/dashboard.html")

def signin(request):

        return render(request,"mh_app/signin.html")

def contact(request):

        return render(request,"mh_app/contact.html")  

def learnmore(request):

        return render(request,"mh_app/learnmore.html")         

