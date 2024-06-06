from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
from .tasks import scrape_coin_data

class StartScrapingView(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        if not coins:
            return Response({'error': 'No coins provided'}, status=status.HTTP_400_BAD_REQUEST)

        task_ids = []
        for coin in coins:
            task = scrape_coin_data.delay(coin)
            task_ids.append(task.id)

        return Response({'task_ids': task_ids}, status=status.HTTP_200_OK)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        result = AsyncResult(job_id)
        if result.state == 'PENDING':
            response = {'status': 'Pending...'}
        elif result.state != 'FAILURE':
            response = {
                'status': result.state,
                'result': result.result
            }
        else:
            response = {
                'status': 'Failed',
                'result': str(result.info),  # This will be the exception raised
            }
        return Response(response, status=status.HTTP_200_OK)
