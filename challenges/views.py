from django.shortcuts import render

# Create your views here.


def challenges_main(request):
    return render(request,"challenges/challenges_main.html")