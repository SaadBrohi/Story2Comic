Story2Comic – Turn Written Stories into Illustrated Comics 📚🎨
Story2Comic is an end-to-end pipeline that uses Large Language Models (LLMs), Stable Diffusion, and Python to convert story texts into comic book panels. The system generates structured scenes with character dialogues and creates matching images with automatically placed dialogue bubbles.

✨ Key Features
🔹 Scene Generation: Breaks stories into individual scenes with LLMs.
🎨 Image Generation: Creates visually rich comic panels using Stable Diffusion.
🖊️ Dialogue Integration: Adds speech bubbles for characters in each panel.
📊 Modular Pipeline: Structured stages for customization and experimentation.
📕 Use Cases
📗 Education: Convert children's stories into engaging visuals.
🎭 Comic prototyping for indie creators.
🤖 Demonstrating multi-modal AI integration (NLP + CV).
🚀 Interactive storytelling or creative content generation.
🔧 Tech Stack
Python
Hugging Face Transformers & Diffusers
LLaMA3 (or OpenChat/LLM of choice)
Stable Diffusion (e.g., dreamshaper-8)
PIL / OpenCV for image manipulation
📂 Folder Structure
story2comic/
├── data/
│   ├── sampled_stories.json         # Input stories
│   └── generated_scenes.json        # LLM-generated scenes and dialogues
├── output/
│   └── scene_{n}.png                # Generated images
├── comic_generator.py               # Scene + dialogue generation logic
├── generate_scenes.py               # LLM API integration
├── text_to_image.py                 # Stable Diffusion image generator
├── generate_images.py               # Create images from prompts
├── add_speech_bubbles.py            # Add dialogues as speech bubbles
└── README.md
🚀 Installation
Clone the repo
git clone https://github.com/yourusername/story2comic.git
cd story2comic
Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Add Hugging Face Token In text_to_image.py, replace:
HF_TOKEN = "your_token_here"
💡 Pipeline Usage
1. Scene Generation from Story
python generate_scenes.py
Uses LLM to break down story into scenes and generate character dialogues.

2. Image Generation
python generate_images.py
Uses Stable Diffusion to convert scene descriptions into comic-style images.

3. Add Speech Bubbles
python add_speech_bubbles.py
Adds randomly placed rounded speech bubbles with dialogues from each scene.

🌐 Prompt Customization Example
In generate_images.py:

prompt = (
  f"{base_prompt}, detailed comic book panel, 2D digital art, "
  "inked outlines, vibrant colors, dramatic pose, shadows and highlights"
)
Change this to control artistic style.

📊 Sample Data
sampled_stories.json
{
  "title": "The Surfer's Journey",
  "sentences": [
    "Kyle walks toward the beach...",
    "Jason jumps from his truck..."
  ]
}
generated_scenes.json
{
  "description": "Kyle, a young adventurer, walks...",
  "dialogues": [
    {"character": "Kyle", "text": "Time to hit the waves!"}
  ]
}
🧳 Output Example
Scene	Description	Image
1	Kyle walking toward the beach	output/scene_1.png
2	Jason grabbing surfboard	output/scene_2.png
🚀 Future Enhancements
 Face or body detection for bubble placement
 Automatic panel layout creation
 Web interface for uploading stories
 TTS (Text-to-Speech) voiceover from dialogues
💼 Author
Saad Brohi Aspiring AI/ML Engineer
📄 License
MIT License

Created with passion for AI storytelling – combining LLMs + Diffusion + Vision tools to bridge text and art.
