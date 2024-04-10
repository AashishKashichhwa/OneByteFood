from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Reservation
# from OneByteFood.models import Reservation

def index(request):
    return render(request, 'index.html')

def reservation(request):
    return render(request, 'reservation.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')


def reserve_table(request):
    reservation_status = None  # Initialize reservation status message

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        num_people = request.POST.get('people')
        comments = request.POST.get('needs')
        payment_option = request.POST.get('payment-option')
        status = 'pending'


        reservation = Reservation(
            name=name,
            phone=phone,
            date=date,
            start_time=start_time,
            end_time=end_time,
            num_people=num_people,
            comments=comments,
            payment_option=payment_option,
            status = status,
        )
        reservation.save()

        messages.success(request, 'Reservation is requested sucessfully. Wait admin to verify the reservation status')
        reservation_status = 'Reservation saved successfully.'  # Update reservation status message

        # Redirect to the same page after form submission
        return HttpResponseRedirect('/reservation/')

    return render(request, 'reservation.html', {'reservation_status': reservation_status})