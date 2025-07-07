# generate_scenes.py

import json
import re
import ollama
import os

def extract_json(text):
    try:
        # Extract the first JSON-like structure from the response
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
    return None

def breakdown_story_into_scenes(sentences, model="llama3"):
    scenes = []

    for i, sentence in enumerate(sentences):
        print(f"\n🧠 Generating scene {i+1}...")

        prompt = f"""
Convert the following sentence into a comic book scene.

Sentence: "{sentence}"

Respond ONLY with a JSON object in the following format:

{{
  "description": "A visual description of the scene.",
  "dialogues": [
    {{ "character": "Character Name", "text": "Dialogue text." }},
    {{ "character": "Another Character", "text": "Another dialogue line." }}
  ]
}}
"""

        try:
            response = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            content = response["message"]["content"].strip()
            scene = extract_json(content)

            # Validate format
            if scene and "description" in scene and "dialogues" in scene:
                # Filter empty or invalid dialogue entries
                valid_dialogues = [
                    d for d in scene["dialogues"]
                    if isinstance(d, dict) and "character" in d and "text" in d and d["character"]
                ]
                if valid_dialogues:
                    scene["dialogues"] = valid_dialogues
                    scenes.append(scene)
                else:
                    print(f"⚠️ No valid dialogues. Skipped.")
            else:
                print(f"⚠️ Invalid format. Skipped.\nRaw:\n{content}\n")

        except Exception as e:
            print(f"⚠️ Error generating scene {i+1}: {e}")

    return scenes

# === MAIN EXECUTION ===

# Load one sampled story from data/sampled_stories.json
with open("data/sampled_stories.json", "r", encoding="utf-8") as f:
    stories = json.load(f)

story = stories[0]
print(f"\n📚 Story Title: {story['title']}")

scenes = breakdown_story_into_scenes(story["sentences"], model="llama3")

# Save results
output_path = "data/generated_scenes.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(scenes, f, indent=2, ensure_ascii=False)

# Print summary
print("\n🎬 Generated Comic Scenes:\n")
for idx, scene in enumerate(scenes, 1):
    print(f"Scene {idx}: {scene['description']}")
    for d in scene["dialogues"]:
        print(f"  {d['character']}: {d['text']}")
