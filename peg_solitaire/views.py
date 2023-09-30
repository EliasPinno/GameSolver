from django.shortcuts import render

# Create your views here.

def solution_view(request):
    return render(request, "pegSolitaire.html")