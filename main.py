from fastapi import FastAPI
from pydantic import BaseModel
import logging

app = FastAPI(title="AI Voice Assistant")

logging.basicConfig(level=logging.INFO)


class InputText(BaseModel):
    text: str

def detect_intent(text: str) -> str:
    """
    A basic intent recognition function using keyword matching.
    Extend this function or integrate with an external NLP API as needed.
    """
    text = text.lower()
    if "weather" in text:
        return "weather inquiry"
    elif "time" in text:
        return "time inquiry"
    elif "joke" in text:
        return "joke request"
    else:
        return "unknown"

@app.post("/predict")
async def predict(input_text: InputText):
    intent = detect_intent(input_text.text)
    
   
    logging.info(f"Received text: {input_text.text} | Detected intent: {intent}")
    
    # (Optional) Save the interaction to a database (MongoDB/PostgreSQL)
    # Example:
    # db.save_interaction({"text": input_text.text, "intent": intent})
    
    return {"intent": intent}
