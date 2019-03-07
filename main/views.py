from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'main/home.html')

def tutorial(request):
    return render(request, 'main/tutorial.html')
