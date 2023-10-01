from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.


def solution_view(request):
    boards = [[[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4]]]
    return render(request, "pegSolitaire.html", {"boards": boards})
