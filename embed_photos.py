import os
import subprocess
import base64

user_uploaded_dir = "/Users/niraj/.gemini/antigravity-ide/brain/b0de3b33-9e9a-4bea-968e-b2fc93e92d86/.user_uploaded"

files = [
    "media_1791027293126.jpg", # 1. Black saree in garden
    "media_1791027408566.jpg", # 2. Mesmerizing eyes close up
    "media_1791027530964.png", # 3. Denim dress & white flowers
    "media_1791027587261.jpg", # 4. Peach floral dress twirl
    "media_1791027782364.jpg", # 5. Black coat & skirt chic
]

output_dir = "/Users/niraj/Desktop/TEST_APPS/sam_birthday/photos"
os.makedirs(output_dir, exist_ok=True)

photos_b64 = []

for i, filename in enumerate(files, 1):
    src_path = os.path.join(user_uploaded_dir, filename)
    dst_img_path = os.path.join(output_dir, f"sam_{i}.jpg")
    
    # Use macOS native sips to resize to max 800px and convert to optimized JPEG
    cmd = [
        "sips",
        "-s", "format", "jpeg",
        "-s", "formatOptions", "80",
        "-Z", "800",
        src_path,
        "--out", dst_img_path
    ]
    subprocess.run(cmd, check=True)
    
    with open(dst_img_path, "rb") as f:
        data = f.read()
    
    b64_str = base64.b64encode(data).decode('utf-8')
    data_url = f"data:image/jpeg;base64,{b64_str}"
    photos_b64.append(data_url)
    
    size_kb = len(data) / 1024
    print(f"Processed Photo {i}: {dst_img_path} ({size_kb:.1f} KB, b64 len: {len(data_url)})")

# Save base64 array to photos_b64.js
with open('/Users/niraj/Desktop/TEST_APPS/sam_birthday/photos_b64.js', 'w', encoding='utf-8') as f:
    f.write("const SAM_PHOTOS_B64 = [\n")
    for b64 in photos_b64:
        f.write(f'  "{b64}",\n')
    f.write("];\n")

print("SUCCESS: Optimized photos generated with sips and saved to photos/ and photos_b64.js!")
