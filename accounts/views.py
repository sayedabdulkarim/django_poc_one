from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            
            # Redirect to next page if provided, otherwise to home
            next_page = request.POST.get('next', '/')
            return redirect(next_page)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email', '')
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Validation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')
        
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return render(request, 'signup.html')
        
        try:
            # Create user - Django automatically checks for duplicate usernames
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, f'Account created successfully for {username}! Please log in.')
            return redirect('login')
            
        except IntegrityError:
            # This handles duplicate username error
            messages.error(request, f'Username "{username}" is already taken. Please choose a different username.')
            return render(request, 'signup.html')
        
        except Exception as e:
            messages.error(request, 'An error occurred. Please try again.')
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')

def logout_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.success(request, f'Goodbye, {username}! You have been logged out.')
    
    return redirect('/')