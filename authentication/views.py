from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from OneByteFoodTeamProject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signup_data

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signup_data

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signup_data

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signup_data

from .models import Signup_data  # Import the model for Signup data

def signup(request):
    if request.method == "POST":
        # Extract data from the POST request
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        
        # Check if passwords match
        if password != confirm_password:
            # Passwords don't match, handle this case (redirect to signup with an error message)
            return render(request, "authentication/signup.html", {'error': 'Passwords do not match'})
        
        # Create a new instance of the Signup_data model and assign values
        new_signup = Signup_data(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        
        # Save the new signup data
        new_signup.save()
        
        # Redirect to signin page after successful signup
        return redirect('signin')
    
    # If request method is not POST, render the signup page
    return render(request, "authentication/signup.html")




def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signup_data

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not (username and password):
            messages.error(request, 'Please provide both username and password')
            return render(request, 'authentication/signin.html')
        
        try:
            # Check if the user exists in the Signup_data table
            user_data = Signup_data.objects.get(username=username)
        except Signup_data.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return render(request, 'authentication/signin.html')
        
        # Check if the password matches
        if user_data.password != password:
            messages.error(request, 'Invalid username or password')
            return render(request, 'authentication/signin.html')

        # Authentication successful, proceed with login
        # Check if the user is an admin or regular user
        if user_data.admin:
            # Redirect the admin user to the admin dashboard
            return redirect('admin_dashboard')
        else:
            # Redirect the regular user to the user dashboard
            return redirect('user_dashboard')
    
    return render(request, 'authentication/signin.html')




def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')


from django.shortcuts import render
from .models import Signup_data  # Import the model
from OneByteFood.models import Reservation  # Import the model

def admin_dashboard(request):
    # Fetch all signup data from the database
    signup_data = Signup_data.objects.all()
    reservations_data = Reservation.objects.all()
    # Pass the signup_data to the template context
    return render(request, "authentication/admin_dashboard.html", {'signup_data': signup_data,'reservations_data':reservations_data})


from django.shortcuts import render

def user_dashboard(request):
    # You can add any necessary logic here to fetch data or perform operations related to the user dashboard
    return render(request, "authentication/user_dashboard.html")


# def display_users(request):
#     user_data = User.objects.all()
#     return render(request, 'admin_dasboard.html', {'user': user_data})

