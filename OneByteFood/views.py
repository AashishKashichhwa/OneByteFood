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


from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from .models import Reservation
from datetime import datetime, time

def reservationDetails(request):
    if request.method == 'POST':
        # Process form submission and save reservation
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        num_people = request.POST.get('people')
        comments = request.POST.get('needs')
        payment_made = request.POST.get('payment_made') == 'on'

        # Initialize status to pending
        status = 'pending'

        # Create the reservation object
        reservation = Reservation(
            name=name,
            phone=phone,
            date=date,
            start_time=start_time,
            end_time=end_time,
            num_people=num_people,
            comments=comments,
            payment_made=payment_made,
            status=status,
        )
        reservation.save()

        messages.success(request, 'Reservation is requested successfully. Wait admin to verify the reservation status')

        # Redirect to the same page after form submission
        return redirect('/reservation_details/?name=' + name + '&phone=' + phone)
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

        # Update status for existing reservations
        current_datetime = datetime.now().time()

        for reservation in reservations_data:
            # Check if payment is made and set status accordingly
            if reservation.payment_made:
                reservation.status = 'confirmed'
            else:
                reservation.status = 'pending'

            # Convert reservation end time string to time object
            reservation_end_time = datetime.strptime(str(reservation.end_time), "%H:%M:%S").time()

            # Check if reservation end time has passed and update status to canceled if payment is not made
            if not reservation.payment_made and current_datetime > reservation_end_time:
                reservation.status = 'cancelled'
            # Otherwise, update status to completed if end time has passed
            elif current_datetime > reservation_end_time:
                reservation.status = 'completed'

            reservation.save()

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
def edit_reservation_user(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    # Handle edit logic here, for example, render an edit form
    return render(request, 'edit_res_user.html', {'reservation': reservation})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    return redirect('admin_dashboard')
def delete_reservation_user(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    
    # Retrieve name and phone from the request.GET dictionary
    name = request.GET.get('name', '')
    phone = request.GET.get('phone', '')

    reservation.delete()
    
    # Redirect to the reservation details page with name and phone parameters
    return redirect('/reservation_details/?name=' + name + '&phone=' + phone)

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
def update_reservation_user(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        reservation.status = new_status
        reservation.save()
        return redirect('reservation')  # Redirect to the admin dashboard after updating status

    return render(request, 'edit_reservation_status.html', {'reservation': reservation})


def user_reservation_history_redirect(request):
    # Redirect to the user_reservation_history.html page
    return render(request, 'user_reservation_history.html')


def show_user_reservation_history(request):
    if request.method == 'GET':
        # If it's a GET request, extract name and phone from the query parameters
        name = request.GET.get('name', '')  
        phone = request.GET.get('phone', '')  
        
        if name and phone:
            # Filter reservations by name and phone number if both are provided
            reservations_data = Reservation.objects.filter(name=name, phone=phone)
        else:
            # If either name or phone number is missing, show all reservations
            reservations_data = Reservation.objects.all()

        # Pass the reservations data to the template along with name and phone
        return render(request, 'user_reservation_history.html', {'reservations_data': reservations_data, 'name': name, 'phone': phone})
    else:
        # If it's not a GET request, redirect to the same page
        return HttpResponseRedirect('/user_reservation_history/')

def cart_view(request):
    # Your cart view logic here
    return render(request, 'cart.html')

from django.shortcuts import render

def birthday(request):
    # Your birthday view logic here
    return render(request, 'birthdaytheme.html')

def unicornR(request):
    # Your unicorn view logic here
    return render(request, 'unicornR.html')

def theme_80(request):
    # Your 80's theme view logic here
    return render(request, 'theme_80.html')

def babybirthday(request):
    # Your baby birthday view logic here
    return render(request, 'babybirthday.html')

