from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone


from django.views.generic import ListView
from django.forms import inlineformset_factory

from django.contrib.auth.decorators import login_required
 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *
from .forms import Albumform, CreateUserForm, MusicianForm
from .decoraters import UserAuth, allowed_user ,admin_only


@UserAuth
def RegisterPage(request):    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account was created" + username)
            return redirect('login')

    context = {'form':form}
    return render(request,'accounts/register.html',context)

@UserAuth
def LoginPage(request):
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,  username = username, password = password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username OR Password Incorrect!......")

    context = {}
    return render(request,'accounts/login.html',context)


def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    today = timezone.now()
    album = Album.objects.all()[:3]
    musician = Musician.objects.all()
    musicianlength = musician.count()

    nober = Album.objects.all().count()
    context={'album':album,'nober':nober, 'musicianlength':musicianlength, 'today':today, 'musician':musician}
    return render(request, 'accounts/home.html', context)


@login_required(login_url='login')
@allowed_user(allowed_user=['customer'])
def UserPage(request):
    album = request.user.musician.album_set.all()
    musician = request.user.musician.first_name
    musicianid = request.user.musician.id
    today = timezone.now()
    
    nober = album.count()
    context={'album':album,'nober':nober, 'today':today,'musician':musician, 'musicianid':musicianid}
    return render(request,'accounts/user-page.html',context)

@login_required(login_url='login')
@allowed_user(allowed_user=['customer'])
def settingPage(request):
    musician = request.user.musician
    form = MusicianForm(instance=musician)

    if request.method == 'POST':
        form = MusicianForm(request.POST, request.FILES, instance=musician)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/account_setting.html', context)


@login_required(login_url='login')
@allowed_user(allowed_user=['admin'])
def AlbumList(request):
    album = Album.objects.all()
    context = {'album':album}
    return render(request, 'accounts/albumlist.html',context)


@login_required(login_url='login')
@allowed_user(allowed_user=['admin'])
def ShowMusician(request,pk):
    musician = Musician.objects.get(id=pk)

    context = {'musician':musician}
    return render(request,'accounts/showmusician.html', context)


@login_required(login_url='login')
@allowed_user(allowed_user=['admin','customer'])
def Createalbum(request,pk):
    musician = Musician.objects.get(id=pk)
    AlbumFormSet = inlineformset_factory(Musician,Album,fields=('name','num_stars','audio_file','season'), extra=5) 
    formset = AlbumFormSet(queryset=Album.objects.none(), instance=musician)
    # form = Albumform()
    if request.method == "POST":
        print(request.POST)
        formset = AlbumFormSet(request.POST,request.FILES,instance=musician)
        if formset.is_valid():
            formset.save()
            return redirect('/',pk = musician.id )
    context = {'form':formset,'musician':musician}
    return render(request,'accounts/createalbum.html', context)



@login_required(login_url='login')
@allowed_user(allowed_user=['admin','customer'])
def Updatemusician(request,pk):
    album = Album.objects.get(id=pk)
    form = Albumform(instance=album)
    context = {'album':album,'form':form}

    if request.method == 'POST':
        # print("here is ",request.POST)
        form = Albumform(request.POST,request.FILES,instance=album)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request,'accounts/update_musician.html', context)


@login_required(login_url='login')
@allowed_user(allowed_user=['admin','customer'])
def Deletealbum(request,pk):
    album = Album.objects.get(id=pk)
    # form = Albumform(instance=album)
    context = {'album':album}

    if request.method == 'POST':
        album.delete()
        return redirect('/')

    return render(request,'accounts/delete.html',context)

