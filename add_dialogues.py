import os
import json
from PIL import Image, ImageDraw, ImageFont

# Load generated scenes
with open("data/generated_scenes.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

# Ensure output/dialogue directory exists
os.makedirs("output/dialogue", exist_ok=True)

# Load font
font_path = "arial.ttf"  # Change if needed
font_size = 14
font = ImageFont.truetype(font_path, font_size)

def draw_dialogue_circle(draw, text, position, font):
    circle_radius = 90
    x, y = position
    padding = 10

    # Draw circle
    left_up = (x, y)
    right_down = (x + circle_radius * 2, y + circle_radius * 2)
    draw.ellipse([left_up, right_down], fill="white", outline="black", width=2)

    # Text wrapping
    max_width = circle_radius * 2 - 2 * padding
    words = text.split()
    lines = []
    line = ""

    for word in words:
        test_line = f"{line} {word}".strip()
        w = font.getbbox(test_line)[2]
        if w <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    lines.append(line)

    # Vertical centering
    line_height = font.getbbox("A")[3] - font.getbbox("A")[1]
    total_height = len(lines) * line_height
    start_y = y + circle_radius - total_height // 2

    for i, line in enumerate(lines):
        line_width = font.getbbox(line)[2]
        text_x = x + circle_radius - line_width // 2
        text_y = start_y + i * line_height
        draw.text((text_x, text_y), line, fill="black", font=font)

# Dialogue bubble positions
# Format: scene_index (1-based): (x, y)
position_map = {
    3: "top-right",  # Scene 3 at top-right
}

def get_position(scene_idx, image):
    bubble_offset_y = 40
    bubble_margin = 30
    radius = 90

    if position_map.get(scene_idx) == "top-right":
        return (image.width - (radius * 2 + bubble_margin), bubble_offset_y)
    else:
        return (bubble_margin, bubble_offset_y)

# Process each image
for idx, scene in enumerate(scenes, 1):
    img_path = f"output/scene_{idx}.png"
    if not os.path.exists(img_path):
        print(f"❌ Missing image: {img_path}")
        continue

    image = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(image)

    dialogue = ""
    for d in scene["dialogues"]:
        if d.get("text", "").strip():
            dialogue = d["text"]
            break

    if dialogue:
        pos = get_position(idx, image)
        draw_dialogue_circle(draw, dialogue, pos, font)

    out_path = f"output/dialogue/scene_{idx}.png"
    image.save(out_path)
    print(f"✅ Dialogue image saved: {out_path}")
