import csv
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Lead

# Verificar se o usuário é superusuário
def is_superuser(user):
    return user.is_superuser

def home(request):
    return render(request, 'home.html')

def process_lead(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']

        lead = Lead(name=name, email=email, phone=phone, course=course)
        lead.save()

        return redirect('thank_you')
    return render(request, 'lead_form.html')

def thank_you(request):
    return render(request, 'thank_you.html')

@user_passes_test(is_superuser)
def admin_leads_view(request):
    leads = Lead.objects.all()
    return render(request, 'admin_leads.html', {'leads': leads})

# Exportar os inscritos em CSV
@user_passes_test(is_superuser)
def export_leads_csv(request):
    leads = Lead.objects.all()

    if not leads.exists():
        return HttpResponse("Nenhum lead registrado para exportar.", content_type="text/plain")

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inscritos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Email', 'Telefone', 'Curso de Interesse'])

    for lead in leads:
        writer.writerow([lead.name, lead.email, lead.phone, lead.course])

    return response

def custom_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta.')
    return redirect('home')