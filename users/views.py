from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Register view
def register(request):
    """Handle user registration."""
    if request.method != 'POST':
        # Display a blank registration form.
        form = UserCreationForm()
    else:
        # Process completed registration form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:home')  # Redirect to home page after successful registration

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'users/register.html', context)

# Login view
# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        # Process login form
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('learning_logs:home')  # Redirect to the home page after successful login
            else:
                # Invalid login credentials
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    # Display the login form (either blank or with errors)
    context = {'form': form}
    return render(request, 'users/login.html', context)



# Logout view
def logout_view(request):
    """Logs the user out and redirects to the home page."""
    logout(request)  # This logs the user out
    return redirect('learning_logs:home')  # Redirect to the home page after logout

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('learning_logs:home')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
