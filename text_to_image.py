from diffusers import StableDiffusionPipeline
import torch
import os
from dotenv import load_dotenv  # 👈 NEW

# ✅ Load variables from .env file
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# Model ID
MODEL_ID = "Lykon/dreamshaper-8"

# Device setup
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DTYPE = torch.float16 if DEVICE == "cuda" else torch.float32

# Load the Stable Diffusion model pipeline with token
print("🔄 Loading Stable Diffusion pipeline...")
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=DTYPE,
    use_auth_token=HF_TOKEN
).to(DEVICE)

print("✅ Pipeline loaded.\n")

# Main function to generate an image from prompt
def generate_image(prompt, output_path):
    image = pipe(prompt).images[0]
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)
    return output_path
