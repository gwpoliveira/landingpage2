import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lead

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

def export_leads(request):
    leads = Lead.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="leads.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Email', 'Telefone', 'Curso'])

    for lead in leads:
        writer.writerow([lead.name, lead.email, lead.phone, lead.course])

    return response