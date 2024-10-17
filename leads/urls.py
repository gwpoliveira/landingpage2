from django.urls import path
from leads import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('lead/', views.process_lead, name='process_lead'),  # Processar lead
    path('thank_you/', views.thank_you, name='thank_you'),  # Página de agradecimento
    path('leads/export/xlsx/', views.export_leads_xlsx, name='export_leads_xlsx'),  # Exportar leads em XLSX
    path('leads/visualizar/', views.admin_leads_view, name='admin_leads'),  # Visualizar leads
    path('login/', views.custom_login, name='login'),  # Login customizado
    path('logout/', views.custom_logout, name='logout'),  # Logout customizado
]
