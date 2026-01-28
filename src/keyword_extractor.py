import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from groq import Groq
from typing import Tuple
import os

class KeywordExtractor:    
    def __init__(self, groq_api_key: str):
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY es requerida")
        
        self.groq_client = Groq(api_key=groq_api_key)
        self.groq_model = "llama-3.1-8b-instant"
        print("Groq API inicializado")
    
    def extract_keywords_with_groq(self, description: str) -> str:
        try:
            response = self.groq_client.chat.completions.create(
                model=self.groq_model,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a visual concept extractor. 
                        Extract 4-8 distinct visual keywords from the user's description.

                        Rules:
                        - Ignore filler words ("I want", "maybe", "kind of")
                        - Focus on: Objects, Colors, Style, Lighting
                        - Return ONLY the keywords separated by spaces.

                        Example Input: "I want a picture of a cute cat sitting on a neon roof in tokyo"
                        Example Output: cute cat neon roof tokyo cyberpunk night"""
                    },
                    {
                        "role": "user",
                        "content": f"Extract keywords from: {description}"
                    }
                ],
                temperature=0.3,
                max_tokens=5,
                top_p=0.9
            )
            
            keywords = response.choices[0].message.content.strip()
            return keywords
            
        except Exception as e:
            print(f"Error con Groq: {e}")
            return description
    
    def extract_keywords(self, description: str) -> Tuple[str, str, str]:
        try:
            print(f"Input original: {description}")
            
            raw_keywords = self.extract_keywords_with_groq(description)
            print(f"Keywords (Groq): {raw_keywords}")
            
            final_summary = raw_keywords + " aesthetic"
            
            return final_summary
            
        except Exception as e:
            print(f"Error en pipeline: {e}")
            return description, "error", "fallback"