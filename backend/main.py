from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from analyzer import analyze_contract
from text_extractor import extract_text_from_file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_file(file.filename, contents)
    results = analyze_contract(text)
    return {"filename": file.filename, "results": results}
