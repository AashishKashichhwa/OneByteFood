from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Reservation, FoodItem
from django.http import JsonResponse
import json
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

from django.shortcuts import render, redirect
from .models import FoodItem, CartItem

def menu_view(request):
    if request.method == 'POST':
        food_item_id = request.POST.get('food_item_id')
        quantity = int(request.POST.get('quantity', 1))
        food_item = FoodItem.objects.get(pk=food_item_id)
        
        # Check if the item already exists in the cart for the current user
        existing_cart_item = CartItem.objects.filter(user=request.user, food_item=food_item).first()
        
        if existing_cart_item:
            # If the item already exists, update the quantity
            existing_cart_item.quantity += quantity
            existing_cart_item.save()
        else:
            # If the item does not exist, create a new CartItem
            cart_item = CartItem.objects.create(user=request.user, food_item=food_item, quantity=quantity)
        
    food_items = FoodItem.objects.all().values('id', 'name', 'price', 'description', 'image_url')
    return render(request, 'menu.html', {'food_items': food_items})

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
    return redirect('/reservation_details/?name=' + reservation.name + '&phone=' + reservation.phone)

def cancel_reservation_user(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    
    # Retrieve name and phone from the request.GET dictionary
    name = request.GET.get('name', '')
    phone = request.GET.get('phone', '')

    reservation.delete()
    
    # Redirect to the reservation details page with name and phone parameters
    return redirect('/user_reservation_history/?name=' + reservation.name + '&phone=' + reservation.phone)


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

from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation

def edit_reservation_user(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'edit_res_user.html', {'reservation': reservation})

def update_reservation_user(request):
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation_id')
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        
        # Update reservation fields
        reservation.name = request.POST.get('name')
        reservation.phone = request.POST.get('phone')
        reservation.date = request.POST.get('date')
        reservation.start_time = request.POST.get('start_time')
        reservation.end_time = request.POST.get('end_time')
        reservation.num_people = request.POST.get('num_people')
        reservation.comments = request.POST.get('comments')
        reservation.payment_made = request.POST.get('payment_made') == 'on'  # Checkbox value handling
        reservation.status = request.POST.get('status')
        
        reservation.save()
        
         # Redirect to the reservation details page with name and phone parameters
    return redirect('/reservation_details/?name=' + reservation.name + '&phone=' + reservation.phone)

    return render(request, 'edit_res_user.html')

def user_reservation_history_redirect(request):
    # Redirect to the user_reservation_history.html page
    return render(request, 'user_reservation_history.html')
# This view handles the user reservation history page

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

from django.shortcuts import render
from .models import CartItem

def cart(request):
    cart_items = CartItem.objects.all()
    total_items = cart_items.count()
    total_price = sum(item.price for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_items': total_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

def add_to_cart(request):
    if request.method == 'POST':
        food_item_id = request.POST.get('food_item_id')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided
        food_item = FoodItem.objects.get(pk=food_item_id)
        total_price = food_item.price * quantity

        # Create a CartItem object and save it to the database
        cart_item = CartItem.objects.create(
            name=food_item.name,
            image_url=food_item.image_url,
            food_item=food_item,
            quantity=quantity,
            price=total_price  # Calculate price based on quantity
        )
        return redirect('menu_redirect')  # Redirect to the cart page
    else:
        return redirect('index')
    
def cart_view(request):
    cart_items = CartItem.objects.all()
    total_items = cart_items.count()
    total_price = sum(item.price for item in cart_items)
    detail_list = []
    for detail in cart_items:
        detail_dict = {
            'id' : detail.id,
            'user' : detail.user, 
            'name' : detail.name,
            'image_url' : detail.image_url, 
            'food_item' : detail.food_item,
            'quantity' : detail.quantity,
            'price' : detail.price
        }
        detail_list.append(detail_dict)
    context = {
        'cart_items': detail_list,
        'total_items': total_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

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

def cartcopy(request):
    # Your baby birthday view logic here
    return render(request, 'cartcopy.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, time
from .models import birthday_theme_reservation  # Importing the model

def reservationTheme(request):
    # Retrieve existing reservations data based on provided name and phone number
    name = request.GET.get('name', '')  
    phone = request.GET.get('phone', '')  

    if name and phone:
        reservations_data = birthday_theme_reservation.objects.filter(name=name, phone=phone)
    else:
        # If either name or phone number is missing, show all reservations
        reservations_data = birthday_theme_reservation.objects.all()

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
        theme = 'unicorn'

        # Convert date and time to datetime objects
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            start_time_obj = datetime.strptime(start_time, '%H:%M').time()
            end_time_obj = datetime.strptime(end_time, '%H:%M').time()
        except ValueError:
            messages.error(request, 'Invalid date or time format.')
            return render(request, 'unicornR.html', context={'reservations_data': reservations_data, 'name': name, 'phone': phone})

        # Combine date and time into datetime for comparison
        start_datetime = datetime.combine(date_obj, start_time_obj)
        end_datetime = datetime.combine(date_obj, end_time_obj)

        # Debugging statements
        print(f"Date: {date_obj}, Start Time: {start_time_obj}, End Time: {end_time_obj}")

        # Check if the date is in the past
        if date_obj < timezone.now().date():
            messages.error(request, 'Cannot reserve a past date.')
            return render(request, 'unicornR.html', context={'reservations_data': reservations_data, 'name': name, 'phone': phone})

        # Check if the end time is before the start time
        if end_datetime <= start_datetime:
            messages.error(request, 'End time must be after start time.')
            return render(request, 'unicornR.html', context={'reservations_data': reservations_data, 'name': name, 'phone': phone})

        # Create the reservation object
        reservation = birthday_theme_reservation(
            name=name,
            phone=phone,
            date=date_obj,
            start_time=start_time_obj,
            end_time=end_time_obj,
            num_people=num_people,
            comments=comments,
            payment_made=payment_made,
            status=status,
        )
        reservation.save()

        messages.success(request, 'Reservation is requested successfully. Wait for admin to verify the reservation status.')

        # Redirect to unicorn_data.html after successful reservation
        return render(request, 'unicorn_data.html', context={'reservations_data': reservations_data})

    return render(request, 'unicornR.html', context={'reservations_data': reservations_data, 'name': name, 'phone': phone})

from django.shortcuts import render
from authentication.models import Signup_data


def user_details(request):
    # Fetch user registration details from the database
    signup_data = Signup_data.objects.all()
    
    # Pass the signup_data to the template context
    return render(request, 'authentication/user_details.html', {'signup_data': signup_data})

from .models import Reservation  # Import the Reservation model

def reservation_details(request):
    # Retrieve all reservation objects from the database
    reservations = Reservation.objects.all()

    # Pass the reservations to the template context
    return render(request, 'authentication/reservation_history.html', {'reservations': reservations})


from django.shortcuts import render
from .models import birthday_theme_reservation

def reservationAdminTheme(request): 
    # Retrieve all reservations data
    reservations_data = birthday_theme_reservation.objects.all()

    return render(request, 'authentication/unicorn_reservation_data.html', context={'reservations_data': reservations_data})

# views.py
# views.py
from django.shortcuts import render, redirect
from .models import Order, Item

def checkout(request):
    if request.method == 'POST':
        try:
            # Get the checkout details from the form
            name = request.POST.get('name')
            place = request.POST.get('place')
            phone = request.POST.get('phone')
            total_items = request.POST.get('total_items')
            total_price = request.POST.get('total_price')

            # Get the cart item details from the form
            item_names = request.POST.getlist('item_names[]')
            item_prices = request.POST.getlist('item_prices[]')
            item_quantities = request.POST.getlist('item_quantities[]')

            # Validate that we have all the item details
            if not (item_names and item_prices and item_quantities and len(item_names) == len(item_prices) == len(item_quantities)):
                return render(request, 'checkout.html', {'error': 'Incomplete item details'})

            # Create Order
            order = Order.objects.create(
                name=name,
                place=place,
                phone=phone,
                total_items=total_items,
                total_price=total_price
            )

            # Create Items
            for i in range(len(item_names)):
                Item.objects.create(
                    order=order,
                    name=item_names[i],
                    price=item_prices[i],
                    quantity=item_quantities[i]
                )

            # Clear cart session data
            if 'cart_items' in request.session:
                del request.session['cart_items']

            # Redirect to the menu page after successful checkout
            return redirect('menu')

        except Exception as e:
            print(f"Error during checkout: {e}")
            return render(request, 'checkout.html', {'error': str(e)})

    return render(request, 'checkout.html')




def delete_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data['id']
        try:
            item = CartItem.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'message': 'Item deleted successfully'}, status=200)
        except CartItem.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
from django.shortcuts import render
from .models import Order

def cart_details(request):
    orders = Order.objects.all()
    return render(request, 'authentication/cart_details.html', {'orders': orders})
