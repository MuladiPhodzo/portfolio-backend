from django.urls import path
from portfolio.views import home  # Import the corrected function

urlpatterns = [
    path('home/', home, name='home'),  # Correct function-based view
]
