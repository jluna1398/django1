from django.urls import path

# look at current directory and look for file
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]


