import os
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

def request_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            #message = render_to_string('appointment_email.html', context)
            send_mail(
            'New Appointment Request',
            'A new appointment request has been submitted.',
            os.getenv('EMAIL_HOST_USER'),
            ['adam.caragine@hotmail.com'],
            html_message=render_to_string('appointment_email.html', context = {
                'name': appointment.name,
                'street': appointment.street,
                'city': appointment.city,
                'state': appointment.state,
                'zip_code': appointment.zip_code,
                'phone_number': appointment.phone_number,
                'reason_for_appointment': appointment.reason_for_appointment,
                'availability': appointment.availability
            })
        )
            return redirect('appointments:appointment_thanks')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/request_appointment.html', {'form': form})

def appointment_thanks(request):
    return render(request, 'appointments/thank_you.html')

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

def admin_appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/admin_appointment_list.html', {'appointments': appointments})

def handle_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        appointment.note = request.POST.get('note', '')
        appointment.save()
        return redirect('appointments:admin_appointment_list')
    return render(request, 'appointments/handle_appointment.html', {'appointment': appointment})
