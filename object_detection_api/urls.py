from django.urls import path
from . import views

urlpatterns = [
    path('objectapi',views.objectapi),
    path('pneumonia_api',views.pneumonia_api),
    path('smart_compose',views.smart_compose),
    path('text_from_textarea',views.text_from_textarea),
    path('report_pdf',views.report_pdf)
]