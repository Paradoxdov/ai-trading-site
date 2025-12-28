import google.generativeai as genai
import re
import os
from .config import GENERATION_CONFIG, SAFETY_SETTINGS, CSS_DIR, MODEL_NAME

class Designer:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS
        )
        self.css_path = os.path.join(CSS_DIR, "ai_theme.css")

    def evolve_design(self):
        print("Designer: Analyzing current visual state...")
        
        with open(self.css_path, "r") as f:
            current_css = f.read()

        # Thesis - Antithesis - Synthesis Loop
        prompt = f"""
        You are the AI Creative Director. Your task is to EVOLVE the website's theme.
        
        CURRENT CSS:
        ```css
        {current_css}
        ```
        
        PROCESS:
        1. THESIS: Propose a new color palette or typo adjustment based on a "Trading Vibe" (e.g., Bull Market Green, Bear Market Red, Volatility Purple).
        2. ANTITHESIS: Critique the current CSS (is it too boring? too bright?).
        3. SYNTHESIS: Output the COMPLETE new CSS file content. 
        
        RULES:
        - KEEP the variable names exactly the same (--bg-color, --text-color, --accent-color, --secondary-color).
        - ONLY change the values of the variables.
        - You can slightly adjust other rules, but do not break the layout.
        - Return ONLY the CSS code block.
        """
        
        try:
            response = self.model.generate_content(prompt)
            new_css = self._extract_css(response.text)
            
            if new_css:
                with open(self.css_path, "w") as f:
                    f.write(new_css)
                print("Designer: Theme evolved.")
            else:
                print("Designer: Failed to extract CSS from synthesis.")
        except Exception as e:
            print(f"Designer Error: {e}")

    def _extract_css(self, text):
        match = re.search(r"```css\s*(.*?)\s*```", text, re.DOTALL)
        if match:
            return match.group(1)
        # Fallback if no code blocks
        return text if "root" in text else None
