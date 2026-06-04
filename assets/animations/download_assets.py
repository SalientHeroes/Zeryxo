import os
import urllib.request

# Create the folder structure if it doesn't exist
os.makedirs("assets/animations", exist_ok=True)

# Stable open-source asset mappings
animations = {
    "pushup.gif": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Push_up_animation.gif",
    "row.gif": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Bodyweight_Inverted_Row.gif",
    "wall_sit.gif": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Wall_Sit_Exercise_Animation.gif",
    "calf_raise.gif": "https://upload.wikimedia.org/wikipedia/commons/3/30/Calf_Raises_Exercise_Animation.gif",
    "lat_pull.gif": "https://upload.wikimedia.org/wikipedia/commons/6/61/Floor_Lat_Pulldown_Animation.gif",
    "wall_angel.gif": "https://upload.wikimedia.org/wikipedia/commons/d/de/Wall_Slides_Exercise_Animation.gif"
}

print("🚀 Starting local animation download sequence for Zeryxo...")
for filename, url in animations.items():
    target_path = os.path.join("assets/animations", filename)
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, target_path)
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")

print("✨ Download sequence complete! Check your assets/animations/ folder.")