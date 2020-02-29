from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, SignUpForm
from datetime import date, datetime, timedelta
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView 
# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ' Tu cuenta ha sido creada')

                return redirect('login')

    context = {'form': form}
    return render(request,'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.info(request, 'Tu nombre o clave es incorrecto')
    
    context= {}
    return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

#Vistas creadas por Gustavo

class SignUpView(CreateView):
    model = Jugador
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/listajuegos/')

class SignInView(LoginView):
    template_name = 'jobs/iniciar_sesion.html'

class SignOutView(LogoutView):
    pass

def buscajuegos(request):
   q = request.GET.get('q', '')
   querys = (Q(cancha__nombre__icontains=q) | Q(cancha__distrito__icontains=q))
   buscajuegos = Juego.objects.filter(querys)
   context = {'data':buscajuegos}
   return render(request, 'buscajuegos.html', context)

def buscacanchas(request):
   q = request.GET.get('q', '')
   querys = (Q(nombre__icontains=q) | Q(distrito__icontains=q))
   buscacanchas = Cancha.objects.filter(querys)
   context = {'data':buscacanchas}
   return render(request, 'buscacanchas.html', context)


def home(request):
    startdate = datetime.today()
    enddate = startdate + timedelta(days=5)
    juegos = Juego.objects.filter(fecha__range=[startdate, enddate])
    context = {'data':juegos}
    return render(request, 'home.html', context)

def listajuegos(request):
    startdate = datetime.today() + timedelta(days=1)
    enddate = date(3000,12,31)
    listajuegos = Juego.objects.filter(fecha__range=[startdate, enddate])
    context = {'data':listajuegos}
    return render(request, 'listajuegos.html',context)

def detail(request,juego_id):
    juego_detail = get_object_or_404(Juego,pk=juego_id)
    context = {'data':juego_detail}
    return render(request,'juego.html', context)

def creajuego(request):
    form = JuegoForm()
    if request.method=='POST':
        form=JuegoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    
    context ={'form':form}
    return render(request,'creajuego.html',context)

def inscripcion(request,juego_id):
    juegodetalle = get_object_or_404(Juego,pk=juego_id)
    clave = request.user.jugador.id
    juegodetalle.jugador.add(clave)
    return redirect('../listajuegos/' + str(juego_id))

def salirdejuego(request,juego_id):
    juegodetalle = get_object_or_404(Juego,pk=juego_id)
    clave = request.user.jugador.id
    juegodetalle.jugador.remove(clave)
    return redirect('../listajuegos/' + str(juego_id))


def listacanchas(request):
    listacanchas = Cancha.objects
    context = {'data':listacanchas}
    return render(request, 'canchas.html',context)

def cancha_detail(request,cancha_id):
    cancha_detail = get_object_or_404(Cancha,pk=cancha_id)
    juegos_cancha = Juego.objects.filter(cancha=cancha_id)
    context = {'data':cancha_detail,'juegos':juegos_cancha}
    return render(request,'canchadetalle.html', context)


@login_required(login_url='sign_in')

def profile(request):
    pelotero = request.user.jugador.id
    juegosprofile = Juego.objects.filter(jugador=pelotero)
    context = {'juegos':juegosprofile}
    return render(request, 'profile.html', context)





