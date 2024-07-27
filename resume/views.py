import os
from django.http import FileResponse, HttpResponse
from django.views.generic import TemplateView, FormView
from resume.forms import ContactForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'index.html'


def open_pdf(request):
    pdf_path = os.path.join('assets', 'pdf', 'My_Resume.pdf')
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')


def download_pdf(request):
    pdf_path = os.path.join('assets', 'pdf', 'My_Resume.pdf')
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="yourfile.pdf"'
        return response


class ContactTemplateView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('resume:success')
    login_url = 'users:login'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        send_mail(
            'Sizga taklifim bor!',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,
            ['sotvoldiyevazamat193@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'succes.html'
    login_url = 'users:login'


