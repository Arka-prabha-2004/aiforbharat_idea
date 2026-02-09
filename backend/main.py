from fastapi import FastAPI
from backend.mock_bedrock import mock_bedrock_response

app = FastAPI()

@app.post("/analyze")
def analyze_content(prompt: str):
    return mock_bedrock_response(prompt)
