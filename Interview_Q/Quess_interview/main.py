
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import string

class ScoreRequest(BaseModel):
    scores: List[float]


app = FastAPI()

@app.post("/evaluate")
def evaluate(request:ScoreRequest):
    return round(sum(request.scores)/len(request.scores),2)


class WordFreq(BaseModel):
    docs:List[str]
    
@app.get("/result")
def wor_document_fre(request:WordFreq):
    for doc in request.docs:
        text = doc.lower().translate(str.maketrans("","",string.punctuation))
        return text