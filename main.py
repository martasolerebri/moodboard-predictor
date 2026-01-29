from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from src.keyword_extractor import KeywordExtractor
from src.scraper import get_live_moodboard

load_dotenv()

app = FastAPI(
    title="Vibe Predictor API",
    description="Groq + T5 pipeline for aesthetic moodboards"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

extractor = KeywordExtractor(groq_api_key=GROQ_API_KEY)

class VibeRequest(BaseModel):
    text: str
    num_images: int = 12

class VibeResponse(BaseModel):
    final_prompt: str     
    images: list

@app.get("/")
async def root():
    return {
        "message": "Vibe Predictor API - Groq + T5 Pipeline",
        "status": "running",
        "pipeline": "Groq (Keywords) → T5 (Refinement)"
    }

@app.post("/predict", response_model=VibeResponse)
async def predict_vibe(request: VibeRequest):
    try:
        final_summary = extractor.extract_keywords(request.text)
        
        print(f"\n{'='*60}")
        print(f"Input: {request.text}")
        print(f"Final: {final_summary}")
        print(f"{'='*60}\n")
        
        images = get_live_moodboard(
            f"{final_summary}  aesthetic", 
            num_images=request.num_images
        )

        display_text = final_summary.replace("aesthetic", "").replace("Aesthetic", "").strip()

        return {
            "final_prompt": display_text,
            "images": images,
        }
        
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "pipeline": "Groq -> T5",
        "groq_available": extractor.groq_client is not None,
        "t5_loaded": extractor.t5_model is not None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=7860,
        reload=False
    )