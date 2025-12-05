from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Entrenador, Gimnasio, Articulo, Habito
from .forms import ContactForm, HabitoForm


# --------------------------
#       HOME
# --------------------------
def home(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')[:3]
    entrenadores = Entrenador.objects.all()[:4]

    context = {
        'articulos': articulos,
        'entrenadores': entrenadores
    }
    return render(request, 'fitness_app/index.html', context)


# --------------------------
#      ENTRENADORES
# --------------------------
def entrenadores(request):
    entrenadores_list = Entrenador.objects.all()
    gimnasios = Gimnasio.objects.all()

    context = {
        'entrenadores': entrenadores_list,
        'gimnasios': gimnasios
    }
    return render(request, 'fitness_app/trainers.html', context)


# --------------------------
#       ARTÍCULOS
# --------------------------
def articulos(request):
    articulos_list = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'fitness_app/articles.html', {'articulos': articulos_list})


# --------------------------
#       CONTACTOS
# --------------------------
def contactos(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, '¡Mensaje enviado correctamente!')
            return redirect('contactos')
    else:
        form = ContactForm()

    return render(request, 'fitness_app/contact.html', {'form': form})


# --------------------------
#  POLÍTICAS DE PRIVACIDAD
# --------------------------
def politicas_privacidad(request):
    return render(request, 'fitness_app/privacy.html')


# --------------------------
#   HÁBITOS Y PROGRESO
# --------------------------
@login_required
def habitos_progreso(request):
    if request.method == 'POST':
        form = HabitoForm(request.POST)
        if form.is_valid():
            habito = form.save(commit=False)
            habito.usuario = request.user
            habito.save()
            messages.success(request, '¡Hábito registrado correctamente!')
            return redirect('habitos_progreso')
    else:
        form = HabitoForm()

    habitos = Habito.objects.filter(usuario=request.user)

    return render(request, 'fitness_app/habits.html',
                  {'form': form, 'habitos': habitos})


# --------------------------
#       LOGIN PERSONALIZADO
# --------------------------
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'fitness_app/login.html', {'form': form})


# --------------------------
#        LOGOUT
# --------------------------
def custom_logout(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')


# --------------------------
#       REGISTRO
# --------------------------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Cuenta creada exitosamente! Bienvenido {user.username}.')
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'fitness_app/register.html', {'form': form})


# --------------------------
#        PROFILE
# --------------------------
@login_required
def profile(request):
    return render(request, "fitness_app/profile.html")
