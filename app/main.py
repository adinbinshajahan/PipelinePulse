import joblib
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

scheduler = BackgroundScheduler()

# store logs
job_logs = []

# ------------------ TASK FUNCTIONS ------------------

def job():
    print(f"Job running at {datetime.now()}")

def train_model():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, "model.pkl")

    accuracy = model.score(X_test, y_test)
    print(f"Model trained. Accuracy: {accuracy}")

    job_logs.append({
        "job": "train_model",
        "time": datetime.now().isoformat(),
        "accuracy": accuracy
    })

# ------------------ SCHEDULER ------------------

@app.on_event("startup")
def start_scheduler():
    scheduler.add_job(job, 'interval', seconds=60)
    scheduler.add_job(train_model, 'interval', minutes=1)
    scheduler.start()

# ------------------ API ROUTES ------------------

@app.get("/")
def home():
    return {"message": "PipelinePulse running 🚀"}

@app.get("/run-job")
def run_job():
    job()
    return {"status": "Job executed"}

@app.get("/train-model")
def run_training():
    train_model()
    return {"status": "Model trained"}

@app.get("/logs")
def get_logs():
    return {
        "total_runs": len(job_logs),
        "logs": job_logs[-10:]  # last 10 runs
    }
@app.get("/predict")
def predict():
    try:
        model = joblib.load("model.pkl")

        sample = [[5.1, 3.5, 1.4, 0.2]]
        prediction = model.predict(sample)[0]

        return {"prediction": int(prediction)}

    except:
        return {"error": "Model not trained yet"}