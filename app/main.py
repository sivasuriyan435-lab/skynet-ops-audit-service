from fastapi import FastAPI, HTTPException
from datetime import datetime
import uuid

app = FastAPI()

events = []

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "skynet-ops-audit-service",
        "timestamp": datetime.utcnow()
    }

@app.post("/events")
def create_event(event: dict):

    required = ["type","tenantId","severity","message","source"]

    for field in required:
        if field not in event:
            raise HTTPException(status_code=400, detail="Missing field")

    event_id = "evt_" + uuid.uuid4().hex[:10]

    event["eventId"] = event_id
    event["storedAt"] = datetime.utcnow()

    events.append(event)

    return {
        "success": True,
        "eventId": event_id
    }

@app.get("/events")
def get_events():
    return {
        "items": events,
        "total": len(events)
    }




