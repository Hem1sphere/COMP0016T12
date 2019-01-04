from django.shortcuts import render
# Create your views here.


def solutions_main(request):
    return render(request,"solutions/solutions_main.html")