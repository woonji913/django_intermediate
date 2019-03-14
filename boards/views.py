from django.shortcuts import render, redirect
from .models import Board
# from pprint import pprint

# Create your views here.
def index(request):
    # pprint(request)
    # pprint(type(request))
    # pprint(dir(request))
    # pprint(request.scheme)
    # pprint(request.get_host())
    # pprint(request.get_full_path())
    # pprint(request.build_absolute_uri())
    # pprint(request.META)
    # pprint(request.method)
    
    boards = Board.objects.order_by('-pk')
    context = {
        'boards': boards,
    }
    return render(request, 'boards/index.html', context)
    
def new(request):
    if request.method == 'POST':
        # post 방식일 때 create
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        # get 방식일 때
        return render(request, 'boards/new.html')

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board': board,
    }
    return render(request, 'boards/detail.html', context)
    
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)
        
def edit(request, pk):
    if request.method == 'POST':
        # update
        board = Board.objects.get(pk=pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
    
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        # edit
        board = Board.objects.get(pk=pk)
        context = {
            'board': board,
            }
        return render(request, 'boards/edit.html', context)