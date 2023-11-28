# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail, get_connection
from django.conf import settings
from django.core.mail import EmailMessage


from .forms import *
from .models import *


class ProjectListAndFormView(SuccessMessageMixin, ListView, FormView):
    model = Project # data from database
    template_name = 'mainpage/main.html'
    context_object_name = 'list_projects' # name of the var in html template
    queryset = Project.objects.all().order_by("-pub_date")#  list of all projects
    object_list = None

    form_class = ContactForm
    success_url = '/' # After submiting the form keep staying on the same url
    success_message = 'Your Form has been successfully submitted!'

    def form_valid(self, form):
        cd = form.cleaned_data

        # Set the "From" address to appear as the user's email
        from_email = cd['email'] if cd['email'] else settings.DEFAULT_FROM_EMAIL

        # Create an EmailMessage instance
        email_message = EmailMessage(
            'Contact Form Submission',  # Subject
            f'Name: {cd["name"]}\nEmail: {cd["email"]}\n\nMessage: {cd["message"]}',
            from_email,
            ['22agrandon@gmail.com'],
            reply_to=[cd['email']] if cd['email'] else [],
        )

        # Send the email
        email_message.send(fail_silently=False)

        return super(ProjectListAndFormView, self).form_valid(form)