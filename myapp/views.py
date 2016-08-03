from django.shortcuts import render

def hallo(request):
   return render(request, "myapp/template/hallo.html", {})

# Create your views here.
