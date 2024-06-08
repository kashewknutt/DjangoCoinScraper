# DjangoCoinScraper

## Introduction

DjangoCoinScraper is a Django-based web application designed to scrape data from a website exposed as a Django REST Framework API. This project was developed as an internship application assignment for shortlisted candidates.

## Getting Started

Follow these steps to set up and use the DjangoCoinScraper project:

## Prerequisites

- Python 3.x installed on your system
- Pip package manager installed
- Redis server installed and running

## Installation

1. **Clone the repository to your local machine**:

    ```bash
    git clone https://github.com/kashewknutt/DjangoCoinScraper.git
    cd DjangoCoinScraper
    ```

2. **Navigate to the project directory**:

    ```bash
    cd DjangoCoinScraper
    ```

3. **Create and activate a virtual environment**:

    ```bash
    python -m venv coinScraper
    source coinScraper/bin/activate  # For Unix/Mac
    coinScraper\Scripts\activate  # For Windows
    ```

4. **Install project dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the Redis server**:

    Open a new terminal and run:

    ```bash
    redis-server
    ```

2. **Run Django migrations to create the database schema**:

    ```bash
    python manage.py migrate
    ```

3. **Start the Celery worker to process scraping tasks**:

    ```bash
    celery -A coin_scraper worker --loglevel=info
    ```

4. **Start the Django development server**:

    ```bash
    python manage.py runserver
    ```

5. **Access the application in your web browser**:

    Open `http://127.0.0.1:8000` to access the web interface.

## Using the Web Interface

1. **Scraping Interface**:

   - Navigate to `http://127.0.0.1:8000/scraper/` to access the scraping page.
   - Enter the coin names you want to scrape (e.g., `bitcoin`, `ethereum`).
   - Submit the form to start scraping.
   - The page will display task IDs for your scraping requests.

2. **Check Scraping Status**:

   - Navigate to `http://127.0.0.1:8000/status/` and enter the task ID to check the current status of your scraping job.

## Using the APIs

You can also use APIs to start scraping and check the status of tasks.

1. **Start Scraping**:

   Use Postman or cURL to send a POST request to start scraping data for specific coins.

   - **Postman**:
     - URL: `http://127.0.0.1:8000/api/taskmanager/start_scraping`
     - Method: POST
     - Body: JSON
       ```json
       {
         "coins": ["bitcoin", "ethereum"]
       }
       ```

   - **cURL**:
     ```bash
     curl -X POST http://127.0.0.1:8000/api/taskmanager/start_scraping -H "Content-Type: application/json" -d '{"coins": ["bitcoin", "ethereum"]}'
     ```

2. **Query Scraping Status**:

   Query the status of scraping tasks with a GET request using Postman or cURL:

   - **Postman**:
     - URL: `http://127.0.0.1:8000/api/taskmanager/scraping_status/<job_id>`
     - Method: GET

   - **cURL**:
     ```bash
     curl http://127.0.0.1:8000/api/taskmanager/scraping_status/<job_id>
     ```

     Replace `<job_id>` with the actual task ID received from the start scraping API.

## Project Structure

- **coinScraper/**: Virtual environment directory (ignored in `.gitignore`)
- **coin_scraper/**: Main Django project folder
  - **api/**: Django app for API and tasks
    - **tasks.py**: Celery tasks for scraping data
    - **views.py**: Views for API endpoints and web pages
  - **templates/**: HTML templates for the web interface
    - `base.html`: Template for the base page
    - `scraper.html`: Template for the scraping page
    - `status.html`: Template for the status page
  - **static/**: Static files like CSS and JavaScript
  - **settings.py**: Project settings
  - **urls.py**: URL configurations
  - **manage.py**: Django's command-line utility for administrative tasks

## Notes

- Ensure Redis is running before starting Celery.
- Update the `settings.py` to configure your database and other settings as needed.
- Use the provided web interface for easy scraping and status checking or interact directly with the APIs for more flexibility.



##Snips:

![image](https://github.com/kashewknutt/DjangoCoinScraper/assets/141485474/227bf083-edfa-4cec-a9f5-99009bb35c30)

![image](https://github.com/kashewknutt/DjangoCoinScraper/assets/141485474/472208ad-1040-43a3-a4e1-0f86dc4df4d1)

![image](https://github.com/kashewknutt/DjangoCoinScraper/assets/141485474/07826894-6568-4670-b56d-6ca49bfbd96a)

![image](https://github.com/kashewknutt/DjangoCoinScraper/assets/141485474/5c4e8b19-825c-441b-9026-cfe88c38a6a2)

