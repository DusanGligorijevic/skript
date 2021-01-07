from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from .models import Fudbaler
from .forms import FudbalerForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Vezbe 13'})
    else:
        return redirect('fudbaleri')


@login_required
def fudbaleri(req):
    tmp = Fudbaler.objects.all()
    return render(req, 'fudbaleri.html', {'fudbaleri': tmp})


@login_required
def fudbaler(req, id):
    tmp = get_object_or_404(Fudbaler, id=id)
    return render(req, 'fudbaler.html', {'fudbaler': tmp, 'page_title': tmp.ime})


@permission_required('change_fudbaler')
def edit(req, id):
    if req.method == 'POST':
        form = FudbalerForm(req.POST)

        if form.is_valid():
            a = Fudbaler.objects.get(id=id)
            a.ime = form.cleaned_data['ime']
            a.prezime = form.cleaned_data['prezime']
            a.godine = form.cleaned_data['godine']
            a.brojNaDresu = form.cleaned_data['brojNaDresu']
            a.tim = form.cleaned_data['tim']
            a.save()
            return redirect('fudbaleri')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Fudbaler.objects.get(id=id)
        form = FudbalerForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('fudbaler')
def new(req):
    if req.method == 'POST':
        print("prvoif")
        form = FudbalerForm(req.POST)

        if form.is_valid():
            print("drugoif")
            a = Fudbaler(ime=form.cleaned_data['ime'], prezime=form.cleaned_data['prezime'],
                         godine=form.cleaned_data['godine'],
                         brojNaDresu=form.cleaned_data['brojNaDresu'], tim=form.cleaned_data['tim'],
                         owner=req.user)
            a.save()
            return redirect('fudbaleri')
        else:
            print("prvoelse")
            return render(req, 'new.html', {'form': form})
    else:
        form = FudbalerForm()
        print("drugoelse")
        return render(req, 'new.html', {'form': form})


def registration(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(req, user)
            return redirect('fudbaleri')
    else:
        form = UserCreationForm()
    return render(req, 'registration.html', {'form': form})


def delete(req, pk):
    fudbaler = Fudbaler.objects.get(id=pk)
    if req.method == "POST":
        fudbaler.delete()
        return redirect('fudbaleri')

    context = {'item': fudbaler}
    return render(req, 'delete.html', context)





