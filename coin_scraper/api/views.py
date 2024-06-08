from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import scrape_coin_data
from celery.result import AsyncResult

class StartScrapingView(APIView):
    def post(self, request):
        print(f"Received request data: {request.data}")
        coins = request.data.get('coins', [])
        if not coins:
            print("No coins provided in request data.")
            return Response({'error': 'No coins provided.'}, status=status.HTTP_400_BAD_REQUEST)
        
        tasks = scrape_coin_data(coins)
        print(tasks)
        #returnedcoins = [task.coin for task in tasks]
        #for task in tasks:
        #    print(task)
        #    returnedcoins += task
        print(f"Started scraping tasks with IDs: {tasks}")
        return Response({'coins': tasks}, status=status.HTTP_202_ACCEPTED)

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
