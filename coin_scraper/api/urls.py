# api/urls.py
from django.urls import path
from .views import ScraperPageView, StartScrapingView, ScrapingStatusView

urlpatterns = [
    path('taskmanager/start_scraping', StartScrapingView.as_view(), name='start_scraping'),
    path('taskmanager/scraping_status/<str:job_id>', ScrapingStatusView.as_view(), name='scraping_status'),
    path('', ScraperPageView.as_view(), name='scraper_page'),
]
