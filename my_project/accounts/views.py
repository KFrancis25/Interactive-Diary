from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib import messages  
from django.core.exceptions import ValidationError
import logging

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#     return render(request, 'accounts/login.html')

# Add this new view function
def home_view(request):
    return render(request, 'demo.html')  # This will render your demo.html template

def account_view(request):
    return render(request, 'accounts/account.html')

def login_view(request):
    if request.method == 'POST':
        email_or_username = request.POST.get('email_or_username')  # Get email or username from the form
        password = request.POST.get('password')

        # Try to find the user by email or username
        try:
            # Check if the input is an email
            if '@' in email_or_username:
                user = User.objects.get(email=email_or_username)  # Get user by email
            else:
                user = User.objects.get(username=email_or_username)  # Get user by username

            # Authenticate the user
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None  # User not found

        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, "Invalid email/username or password")  # Show error message

    return render(request, 'accounts/login.html')

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one number.")
    if not any(char in "!@#$%^&*()_+" for char in password):
        errors.append("Password must contain at least one special character.")
    return errors

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'accounts/signup.html')

        # Validate password
        password_errors = validate_password(password)
        if password_errors:
            for error in password_errors:
                messages.error(request, error)
            return render(request, 'accounts/signup.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'accounts/signup.html')

        # Create user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, "An error occurred during signup")
            return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')


#original Signup view
# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         # Check if passwords match
#         if password != confirm_password:
#             messages.error(request, "Passwords do not match")
#             return render(request, 'accounts/signup.html')

#         # Validate password
#         password_errors = validate_password(password)
#         if password_errors:
#             for error in password_errors:
#                 messages.error(request, error)
#             return render(request, 'accounts/signup.html')

#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists")
#             return render(request, 'accounts/signup.html')

#         # Create user
#         try:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             messages.success(request, "Account created successfully! Please log in.")
#             return redirect('login')
#         except Exception as e:
#             messages.error(request, "An error occurred during signup")
#             return render(request, 'accounts/signup.html')

#     return render(request, 'accounts/signup.html')

# @csrf_protect
# @require_http_methods(["POST"])
# def custom_login(request):
#     form = SecureAuthenticationForm(request, data=request.POST)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             user.reset_login_attempts()
#             logger.info(f"User {username} logged in successfully")
#             return redirect('home')
#         else:
#             user = CustomUser.objects.filter(username=username).first()
#             if user:
#                 user.increase_login_attempts()
#                 logger.warning(f"User {username} failed to log in")

#     logger.error('Login attempt failed')
#     return render(request, 'login.html', {'form': form})

