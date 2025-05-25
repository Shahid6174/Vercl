from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Enable CORS for all origins (GET only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks data once on startup
with open("q-vercel-python.json", "r") as f:
    marks_data = json.load(f)  # dict of {name: mark}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    # Return marks in the order of requested names
    result = []
    for n in name:
        mark = marks_data.get(n)
        if mark is None:
            result.append(None)  # or 0 if you prefer
        else:
            result.append(mark)
    return {"marks": result}
