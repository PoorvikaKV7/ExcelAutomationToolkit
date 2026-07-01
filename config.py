import os

# ==========================================
# Project Folder Configuration
# ==========================================

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"
LOG_FOLDER = "logs"
ASSETS_FOLDER = "assets"

# ==========================================
# Create folders if they don't exist
# ==========================================

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(ASSETS_FOLDER, exist_ok=True)