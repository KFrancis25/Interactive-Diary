# from django.shortcuts import render

# def login_view(request):
#     return render(request, 'accounts/login.html')

# def signup_view(request):
#     return render(request, 'accounts/signup.html')

# def account_view(request):
#     return render(request, 'account.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
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
    return render(request, 'accounts/login.html')

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

