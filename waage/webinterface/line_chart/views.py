from django.shortcuts import render


def line_chart(request):
    return render(request, "line_chart/line_chart.html",{})


# Create your views here.
