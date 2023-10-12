from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('listing.urls', namespace='listing')),  # Include URL patterns from the 'listing' app
]
