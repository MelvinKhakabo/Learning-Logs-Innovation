from django.shortcuts import render

def home_view(request):
    """Display the home page."""
    return render(request, 'home.html')  # This assumes you have a home.html template
