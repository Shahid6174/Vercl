from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load student marks from JSON
students = {}
with open('q-vercel-data.json', mode='r') as file:
    data = json.load(file)
    for entry in data:
        students[entry['name']] = int(entry['marks'])

@app.get("/api")
async def get_marks(name: List[str]):
    if not name:
        raise HTTPException(status_code=400, detail="At least one name is required")
    
    marks = []
    for n in name:
        if n in students:
            marks.append(students[n])
        else:
            raise HTTPException(status_code=404, detail=f"Student {n} not found")
    
    return {"marks": marks}