from fastapi import FastAPI
from data.logs import generate_logs
from core.sorting import sort_logs
from core.analyzer import count_by_level, count_by_service
from database.storage import Storage

app = FastAPI()
db = Storage()

@app.get("/logs")
def get_logs():
    return db.get_all_as_dicts()

@app.get("/logs/sorted")
def get_logs_sorted():
    logs = db.get_all_as_dicts()
    return sort_logs(logs)

@app.get("/logs/errors")
def get_errors():
    logs = db.get_all_as_dicts()
    return {
        "by_level": count_by_level(logs),
        "by_service": count_by_service(logs)
    }

@app.post("/logs/seed")
def seed_logs():
    logs = generate_logs(10)
    for log in logs:
        db.insert(log)
    return {"message": "10 logs inseridos com sucesso!"}
