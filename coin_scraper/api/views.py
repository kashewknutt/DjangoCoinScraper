import logging
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import scrape_coin_data  # Assuming your task is defined here
from celery.result import AsyncResult

logger = logging.getLogger(__name__)

class StartScrapingView(APIView):
    def post(self, request):
        logger.debug(f"Received request data: {request.data}")
        coins = request.data.get('coins', [])
        if not coins:
            logger.debug("No coins provided in request data.")
            return Response({'error': 'No coins provided.'}, status=status.HTTP_400_BAD_REQUEST)
        
        task = scrape_coin_data.delay(coins)  # Start the Celery task
        logger.debug(f"Started scraping task with ID: {task.id}")
        return Response({'job_id': task.id}, status=status.HTTP_202_ACCEPTED)


class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        task = AsyncResult(job_id)
        if task.state == 'SUCCESS':
            return Response(task.result, status=status.HTTP_200_OK)
        else:
            return Response({'status': task.state}, status=status.HTTP_200_OK)


# Function views for rendering templates

def home_view(request):
    return render(request, 'home.html')

def scraper_view(request):
    return render(request, 'scraper.html')

def status_view(request):
    return render(request, 'status.html')
