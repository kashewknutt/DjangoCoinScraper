DjangoCoinScraper
Introduction
DjangoCoinScraper is a Django-based web application designed to scrape data from a website exposed as a Django REST Framework API. This project was developed as an internship application assignment for shortlisted candidates.

Getting Started
Follow these steps to set up and use the DjangoCoinScraper project:

Prerequisites
Python 3.x installed on your system
Pip package manager installed
Redis server installed and running
Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/DjangoCoinScraper.git
Navigate to the project directory:
bash
Copy code
cd DjangoCoinScraper
Create and activate a virtual environment (optional but recommended):
bash
Copy code
python -m venv env
source env/bin/activate
Install project dependencies:
Copy code
pip install -r requirements.txt
Running the Application
Start the Redis server:
Copy code
redis-server
Run Django migrations to create the database schema:
Copy code
python manage.py migrate
Start the Celery worker to process scraping tasks:
css
Copy code
celery -A coin_scraper worker --loglevel=info
Start the Django development server:
Copy code
python manage.py runserver
Access the application in your web browser at http://127.0.0.1:8000.
Using the APIs
Use Postman or cURL to send a POST request to start scraping data for specific coins:
makefile
Copy code
URL: http://127.0.0.1:8000/api/taskmanager/start_scraping
Method: POST
Body: JSON
{
  "coins": ["bitcoin", "ethereum"]
}
Query the status of scraping tasks with a GET request:
vbnet
Copy code
URL: http://127.0.0.1:8000/api/taskmanager/scraping_status/<job_id>
Method: GET