import google.generativeai as genai
import re
from .config import GENERATION_CONFIG, SAFETY_SETTINGS, MODEL_NAME

class ImageGenerator:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS
        )

    def generate_svg(self, prompt_description):
        print(f"ImageGen: Coding an SVG for '{prompt_description}'...")
        prompt = f"""
        You are an AI Generative Artist.
        Create a SCALABLE VECTOR GRAPHIC (SVG) code for this concept: "{prompt_description}".
        
        Style: Abstract, Cyberpunk, Data Visualization, Geometric.
        Colors: Use neon greens, dark grays, and transparency.
        Dimensions: 800x400.
        
        Output ONLY the raw <svg>...</svg> code. No markdown code blocks.
        """
        try:
            response = self.model.generate_content(prompt)
            clean_svg = self._clean_svg_output(response.text)
            return clean_svg
        except Exception as e:
            print(f"ImageGen Error: {e}")
            return None

    def _clean_svg_output(self, text):
        # Remove markdown triggers if present
        text = text.replace("```xml", "").replace("```svg", "").replace("```", "")
        # Find start and end of svg tag
        start = text.find("<svg")
        end = text.find("</svg>") + 6
        if start != -1 and end != -1:
            return text[start:end]
        return None
