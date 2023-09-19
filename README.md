# Toxic Comment Classifier

This application serves as an interface for a toxic comment classification system. The system classifies comments based on their toxic nature using a pre-trained Tensorflow model. It includes both a backend built with FastAPI and a frontend constructed using Streamlit.

## Backend

### Tech Stack:

- **FastAPI** - For API creation
- **Tensorflow** - To predict comment toxicity
- **PostgreSQL** - For logging each endpoint hit
- **asyncpg** - Asynchronous PostgreSQL interaction for FastAPI

### Features:

1. **Comment Endpoint**: Accepts a string as input, returns the same string appended with toxicity labels based on the classification done by the Tensorflow model.
2. **CSV Endpoint**: Accepts a CSV file containing comments (a required `column_text` for comments). It responds with a CSV file containing the comments along with their respective toxicity labels.
3. **Logging**: Every hit on these endpoints is logged to a PostgreSQL database. The log includes the query, response, and timestamp.

### Configuration:

Database settings can be modified in `backend/.env`.

Backend-specific configurations can be found in `backend/app/data/config.py`.

## Frontend

### Tech Stack:

- **Streamlit** - For creating the web interface

### Features:

1. **Text Submission**: Users can submit a text, which gets sent to the comment endpoint of the backend. The toxicity labels provided by the model are then displayed on the page.
2. **CSV Submission**: Users can upload a CSV file. Once processed, a download button appears allowing users to download the classified CSV with the toxicity labels.

### Configuration:

Frontend-specific configurations can be found in `frontend/app/data/config.py`.

## Deployment using Docker:

The repository includes `backend/Dockerfile`, `frontend/Dockerfile`, and `docker-compose.yaml` to facilitate easy deployment using Docker.

## **Initial Setup**:

Before starting the application, download the model weights:

1. Download the model weights from [this link](https://drive.google.com/file/d/1IAwkmnuXiuBLUYnQn7t613Mi6LcZDO-n/view?usp=drive_link).
2. Place the downloaded weights into the `backend/app/data` directory.


## Setup and Run:

1. Clone the repository.
2. Navigate to the project directory.
3. Ensure you have Docker and docker-compose installed.
4. Run `docker-compose up` to start both backend and frontend services.

For any additional details or issues, please refer to the individual configuration files or raise an issue on the repository.
