from django.shortcuts import render
import datetime

def post_list(request):
    heut = datetime.datetime.now().date()
    return render(request, "myapp/post_list.html", {"today":heut})


# Create your views here.
