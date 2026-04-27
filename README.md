# PipelinePulse

PipelinePulse is a lightweight **machine learning pipeline system** built with FastAPI.
It supports model training, prediction, scheduled jobs, and a simple web interface.

## Features

*  FastAPI backend for high-performance APIs
*  Machine Learning model (Random Forest on Iris dataset)
*  Background scheduler using APScheduler
*  API endpoints for training, prediction, and logs
*  Simple frontend UI for interacting with the system

## Project Structure

```
PipelinePulse/
│
├── app/
│   ├── main.py
│   └── templates/
│       └── index.html
│
├── requirements.txt
├── Dockerfile
└── .gitignore
```

## How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/PipelinePulse.git
cd PipelinePulse
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the server

```
python -m uvicorn app.main:app --reload
```

### 4. Open in browser

```
http://127.0.0.1:8000
```

## API Endpoints

| Endpoint       | Description                |
| -------------- | -------------------------- |
| `/`            | Frontend UI                |
| `/train-model` | Train ML model             |
| `/predict`     | Get prediction             |
| `/run-job`     | Run scheduled job manually |
| `/logs`        | View recent job logs       |

## Machine Learning

* Dataset: Iris dataset (from sklearn)
* Model: RandomForestClassifier
* Task: Classification

## Scheduler

* Runs background jobs using APScheduler
* Example jobs:

  * Periodic logging
  * Model retraining

## Limitations

* No database (logs stored in memory)
* Basic UI (not production-ready)
* No authentication/security

## Future Improvements

* Add database (PostgreSQL / SQLite)
* Improve frontend (React or better UI)
* Add user input for predictions
* Deploy to cloud (Render / Railway)

## Tech Stack

* FastAPI
* APScheduler
* Scikit-learn
* HTML (basic frontend)

## Author

Adin Bin Shajahan

##
