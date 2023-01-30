from decouple import config
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ContactForm


class ContactView(View):
    template_name = "contact/contact.html"

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # contact = form.save()
            print()
            print(request.POST["fullname"])
            print(request.POST["email"])
            print(request.POST["message"])
            print()

            send_mail(
                # Subject
                f"New Contact Form Message from, {request.POST['fullname']}",
                # Content
                request.POST["message"],
                # Sender's email
                config("SEND_TO"),
                # Recipient(s)
                ["dkibui@outlook.com"],
                fail_silently=False,
            )

            return redirect(reverse("contact:index"))
        return render(request, self.template_name, {"form": form})
