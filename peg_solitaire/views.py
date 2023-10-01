from django.shortcuts import render
from django.template.loader import render_to_string
from render_board import GridSolitaireUtilities as gs

# Create your views here.


def solution_view(request):
    solution = gs.getSolution()
    boards = gs.getAllBoardsInSolution(gs.startingBoard, solution)
    #boards = [[[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4]]]
    return render(request, "pegSolitaire.html", {"boards": boards})
