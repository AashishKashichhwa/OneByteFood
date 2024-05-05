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


from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Reservation

def reservationDetails(request):
    if request.method == 'POST':
        # Process form submission and save reservation
        reservation_status = None  # Initialize reservation status message
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
            status=status,
        )
        reservation.save()

        messages.success(request, 'Reservation is requested successfully. Wait admin to verify the reservation status')
        reservation_status = 'Reservation saved successfully.'  # Update reservation status message

        # Redirect to the same page after form submission
        return HttpResponseRedirect('/reservation_details/?name=' + name + '&phone=' + phone)
    else:
        # If it's a GET request or no POST data is sent, show reservations for the user
        name = request.GET.get('name', '')  # Get name from GET request, with a default value of empty string
        phone = request.GET.get('phone', '')  # Get phone from GET request, with a default value of empty string

        if name and phone:
            # Filter reservations by name and phone number if both are provided
            reservations_data = Reservation.objects.filter(name=name, phone=phone)
        else:
            # If either name or phone number is missing, show all reservations
            reservations_data = Reservation.objects.all()

        # Pass the reservations data to the template
        return render(request, 'reservation.html', {'reservations_data': reservations_data, 'name': name, 'phone': phone})


def menu_redirect(request):
    # Redirect to the menu.html page
    return render(request, 'menu.html')

def events_redirect(request):
    # Redirect to the menu.html page
    return render(request, 'events.html')

def gallery_redirect(request):
    # Redirect to the menu.html page
    return render(request, 'gallery.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation

def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    # Handle edit logic here, for example, render an edit form
    return render(request, 'edit_reservation.html', {'reservation': reservation})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    return redirect('admin_dashboard')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from django.contrib import messages

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation

def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        reservation.status = new_status
        reservation.save()
        return redirect('admin_dashboard')  # Redirect to the admin dashboard after updating status

    return render(request, 'edit_reservation_status.html', {'reservation': reservation})
