import sendgrid
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ContactForm


class ContactView(View):
    template_name = 'contact/contact.html'
    form_class = ContactForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect(reverse('contact:index'))
        return render(request, self.template_name, {'form': form})
