from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)
    
def create(request):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board = Board()
            board.title = board_form.cleaned_data.get('title')
            board.content = board_form.cleaned_data.get('content')
            board.save()
            return redirect(board)
    else:
        board_form = BoardForm()
    context = {'board_form':board_form}
    return render(request, 'boards/form.html', context)
    
def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    board.hit += 1
    board.save()
    context = {
        'board': board
    }
    return render(request, 'boards/detail.html', context)
    
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect(board)
        
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board.title = board_form.cleaned_data.get('title')
            board.content = board_form.cleaned_data.get('content')
            board.save()
            return redirect(board)
    else:
        board_form = BoardForm(initial=board.__dict__)
    context = {'board_form': board_form}
    return render(request, 'boards/form.html', context)