import os
import urllib.request

# Create the animations directory if it doesn't exist
os.makedirs("animations", exist_ok=True)

# Stable Wikimedia open CDN endpoints
links = {
    "pushup.gif": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Push_up_animation.gif",
    "row.gif": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Bodyweight_Inverted_Row.gif",
    "wall_sit.gif": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Wall_Sit_Exercise_Animation.gif",
    "calf_raise.gif": "https://upload.wikimedia.org/wikipedia/commons/3/30/Calf_Raises_Exercise_Animation.gif",
    "lat_pull.gif": "https://upload.wikimedia.org/wikipedia/commons/6/61/Floor_Lat_Pulldown_Animation.gif",
    "wall_angel.gif": "https://upload.wikimedia.org/wikipedia/commons/d/de/Wall_Slides_Exercise_Animation.gif"
}

print("🚀 Initializing Zeryxo Secure Asset Streaming Core...")

for filename, url in links.items():
    target_path = os.path.join("animations", filename)
    print(f"Streaming {filename}...")
    
    try:
        # Create a request object and mask it with a standard browser User-Agent header
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        
        # Read the file data from the stream and write it directly to your folder
        with urllib.request.urlopen(req) as response:
            with open(target_path, "wb") as local_file:
                local_file.write(response.read())
        print(f"✅ Success: {filename} saved safely.")
        
    except Exception as e:
        print(f"❌ Critical Error on {filename}: {e}")

print("\n✨ Download sequence finalized! Run 'git status' to check your workspace changes.")