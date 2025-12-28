import google.generativeai as genai
import os
from .config import GENERATION_CONFIG, SAFETY_SETTINGS, MODEL_NAME

class Writer:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS
        )

    def write_article(self, topic_data):
        topic = topic_data['title']
        print(f"Writer: Drafting article on '{topic}'...")
        
        # Thesis: Write the article
        prompt = f"""
        You are an autonomous AI trading administrator for a high-end trading blog.
        Write a SHORT, cynical, and highly analytical blog post about '{topic}'.
        
        Style guidelines:
        - Professional but edgy tone.
        - Focus on data and logic, despise emotion.
        - Use Markdown formatting.
        - Structure: H2 for subtitles, bold for key terms.
        - Length: Around 300-500 words.
        - End with a unique "AI Verdict" box.
        
        Do not include the main Title (H1) in the output, just the body.
        """
        
        try:
            response = self.model.generate_content(prompt)
            content = response.text
            
            # Anti-thesis & Synthesis (Self-Correction/Fact Checking simulation)
            # In a real loop, we would act on this. For now, we trust the "brain" to be smart enough once.
            
            return content
        except Exception as e:
            print(f"Writer Error: {e}")
            return "Error generating content. The market is too volatile for words right now."

    def generate_image_prompt(self, topic):
        print(f"Writer: Dreaming up an image for '{topic}'...")
        prompt = f"""
        Create a prompt for an AI image generator (like Imagen or Midjourney) 
        to create a header image for an article about '{topic}'. 
        The style should be: "Cyberpunk finance, dark background, neon data lines, abstract, high tech".
        Return ONLY the prompt string.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return "Abstract trading chart, neon colors, dark background"
