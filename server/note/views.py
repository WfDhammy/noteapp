from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        username = request.POST['signup_username']
        email = request.POST['signup_email']
        password1 = request.POST['signup_password1']
        password2 = request.POST['signup_password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=make_password(password1))
            user.set_password(password1)
            user.save()
            return redirect('login')
    return render(request, 'signup.html')



def main(request):
    
     return render(request, 'landing.html', )





def logout_user(request):
    logout(request)
    return redirect('login')
  


def login_user(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = authenticate(username=username, password=password)
        if user.is_authenticated:
            login(request, user)
            return redirect('create_note')
        return render(request, 'landing.html')
    return render(request, 'login.html')


@login_required
def detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'about.html',{'note':note})

@login_required
def note_list(request):
    user = request.user
    notes = Note.objects.filter(user=user)
    return render(request, 'saved.html',  {'notes': notes})


@login_required  # this decorator will ensure that only authenticated users can access this view.
def create_note(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Note.objects.create(title=title, content=content, user=user)
        note.save()
        print("note created")
        return redirect('note_list') 
    return render(request, 'note.html')

@login_required
def edit(request,  note_id):
    user = request.user
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note.title = title
        note.content = content
        note.save()
        return redirect('note_list')
    return render(request, 'edit.html', {'note': note})

@login_required
def delete(request, note_id):
    user = request.user
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('note_list')
