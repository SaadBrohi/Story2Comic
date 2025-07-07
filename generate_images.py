import json
from text_to_image import generate_image

# Load generated scenes
with open("data/generated_scenes.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

print(f"\n🎨 Generating Comic Images from {len(scenes)} Scenes...\n")

for idx, scene in enumerate(scenes, 1):
    base_prompt = scene["description"]
    prompt = (
        f"{base_prompt}, detailed comic book panel, 2D digital art, "
        "inked outlines, vibrant colors, dramatic pose, shadows and highlights, professional comic art style"
    )
    output_path = f"output/scene_{idx}.png"

    print(f"🖼️ Scene {idx}: {prompt}")
    generate_image(prompt, output_path)
    print(f"✅ Image saved to {output_path}\n")
