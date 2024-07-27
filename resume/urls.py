from django.urls import path

from resume import views
from resume.views import HomePageView, ContactTemplateView, ThankYouView

app_name = 'resume'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('open-pdf/', views.open_pdf, name='open_pdf'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('success/',ThankYouView.as_view(), name='success'),

]