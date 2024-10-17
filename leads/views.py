import openpyxl
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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        consultores = request.POST.get('consultores')

        lead = Lead(name=name, email=email, phone=phone, course=course, consultores=consultores)
        lead.save()

        return redirect('thank_you')
    return render(request, 'home.html')

def thank_you(request):
    return render(request, 'thank_you.html')

@user_passes_test(is_superuser)
def admin_leads_view(request):
    leads = Lead.objects.all()
    return render(request, 'admin_leads.html', {'leads': leads})


@user_passes_test(lambda u: u.is_superuser)
def export_leads_xlsx(request):
    # Criar um workbook e a worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inscritos"

    # Definir os cabeçalhos da planilha
    ws.append(['Nome', 'Email', 'Telefone', 'Curso de Interesse', 'Consultor'])

    # Obter os dados dos leads
    leads = Lead.objects.all()

    # Adicionar os dados de cada lead na planilha
    for lead in leads:
        ws.append([lead.name, lead.email, lead.phone, lead.course, lead.consultores])

    # Definir a resposta HTTP com o arquivo XLSX
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=inscritos.xlsx'

    # Salvar o workbook na resposta
    wb.save(response)

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

