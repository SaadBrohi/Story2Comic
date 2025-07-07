# sample_stories.py

import csv
import json
import random
import os

input_path = "data/rocstories.csv"
output_path = "data/sampled_stories.json"

# Read all stories from the CSV
stories = []
with open(input_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        story = {
            "id": row["storyid"],
            "title": row["storytitle"],
            "sentences": [
                row["sentence1"],
                row["sentence2"],
                row["sentence3"],
                row["sentence4"],
                row["sentence5"],
            ]
        }
        stories.append(story)

# Randomly sample 5 stories
sampled_stories = random.sample(stories, 5)

# Save to JSON
os.makedirs("data", exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(sampled_stories, f, indent=2)

print("✅ Sampled stories saved to", output_path)
