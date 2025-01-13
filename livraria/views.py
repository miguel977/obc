from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Book

# Create your views here.

def home(request):
    books = Book.objects.all()
    if request.method == "POST":
        username = request.POST['usuario']
        password = request.POST['senha']
        # Autenticando
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(request, 
                "Login realizado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, 
                "Erro na autenticação. Tente novamente!")
            return redirect('home')
    else:
        return render(request, 'home.html', {'books':books})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(
        request, 
        "Você fez o logout com sucesso!"
    )
    return redirect('home')

def register_user(request):
    if request.method == "POST ":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Você fez login com sucesso com novo usuário")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def book_detail(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        return render(request, 'book.html', {'book': book})
    
    else:
        messages.error(request, 'você precisa está logado') 
        return redirect('home')
    
def book_delete(request,id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        book.delete()
        messages.success(request, 'Livro foi excluido com sucesso')
        return redirect('home')
    else:
        messages.error(request, 'Você precisa está logado')
        return redirect('home')
