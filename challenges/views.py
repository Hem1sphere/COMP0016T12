from django.shortcuts import render

# Create your views here.


def challenges_dev_main(request):
    return render(request,"challenges/challenges_developers_main.html")

def challenges_dev_detail(request):
    return render(request,"challenges/challenges_developers_detail.html")