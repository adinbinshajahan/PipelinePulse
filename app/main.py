from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = FastAPI()

scheduler = BackgroundScheduler()

def job():
    print(f"Job running at {datetime.now()}")

scheduler.add_job(job, 'interval', seconds=60)
scheduler.start()

@app.get("/")
def home():
    return {"message": "PipelinePulse running 🚀"}

@app.get("/run-job")
def run_job():
    job()
    return {"status": "Job executed"}