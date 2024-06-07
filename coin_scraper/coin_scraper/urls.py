"""
URL configuration for coin_scraper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# coin_scraper/urls.py

from django.contrib import admin
from django.urls import include, path
from api.views import home_view, scraper_view, status_view, ScrapingStatusView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API routes under /api/
    path('', home_view, name='home'),  # Root URL directs to home view
    path('scraper/', scraper_view, name='scraper'),  # Scraper page URL
    path('status/', status_view, name='status'),  # Status page URL
    path('api/taskmanager/scraping_status/<job_id>/', ScrapingStatusView.as_view(), name='scraping_status'),
]
