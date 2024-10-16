from django.urls import path
from leads import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('lead/', views.process_lead, name='process_lead'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('export-leads/', views.export_leads, name='export_leads'),
]
